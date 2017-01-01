import numpy as np
from pymongo import MongoClient
import pyaudio
import click
from bunch import Bunch


db = MongoClient("sqwak.kingofthestack.com")

def get_unrated_sample():
    result = db.sqwaks.sounds.find_one({
        "rating": None
    })
    db_amps = np.array(result["amplitudes"])
    return Bunch({
        "amplitudes": db_amps,
        "id": result["_id"]
    })


def rate_sample(id, rating):
    db.sqwaks.sounds.update_one({
        "_id": id
    }, {
        '$set': {
            "rating": rating
        }
    }, upsert=False)


def play(amplitudes):
    p = pyaudio.PyAudio()

    playback_settings = {
        'format': pyaudio.paFloat32,
        'channels': 1,
        'rate': 44100,
        'output': True,
        'output_device_index': 1
    }

    stream = p.open(**playback_settings)

    # Assuming you have a numpy array called samples
    data = amplitudes.astype(np.float32).tostring()
    stream.write(data)


""" Defines a custom param type for click's input validation """
class FloatInRangeParamType(click.ParamType):
    
    def __init__(self, min_float=0.0, max_float=1.0):
        self.min_float = min_float
        self.max_float = max_float

    def convert(self, value, param, ctx):
        try:
            number = float(value)
            if (number >= self.min_float and number <= self.max_float):
                return number
            else:
                raise ValueError()
        except ValueError:
            self.fail('%s is not a float within the given range' % value, param, ctx)

def main():
    is_rating = True
    FLOAT_IN_RANGE = FloatInRangeParamType()
    while(is_rating):
        if click.confirm('Do you want to continue?'):
            sample = get_unrated_sample()
            play(sample.amplitudes)
            rating = click.prompt('Rate that sqwak! (0.0 - 1.0)', type=FLOAT_IN_RANGE)
            rate_sample(sample.id, rating)
        else:
            click.echo("Goodbye!")
            is_rating = False

if(__name__ == "__main__"):
    main()