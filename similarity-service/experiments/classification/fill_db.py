from bokeh.plotting import figure, show, output_file
import bokeh.layouts
import bokeh.models
import bokeh.embed
import bokeh.models.widgets
import bokeh.resources
import pandas as pd
import scipy.io.wavfile
import os
import numpy as np
import wavio
import pickle
from pymongo import MongoClient
import redis
import pdb

db = MongoClient()

def main():
    # this is a pandas DF
    urban_sound = load_from_csv(fold=10)

    db.urban_sound.audio.insert_many(urban_sound.to_dict('records'))

    # results = db.urban_sound.fold1.find({ 'fold': 1 })
    # urban_sound = pd.DataFrame(list(results))

# print urban_sound.head(5)
def load_from_csv(fold):
    dir = os.path.dirname(__file__)
    csv_path = os.path.join(dir, 'UrbanSound8K', 'metadata', 'UrbanSound8K.csv')
    urban_sound = pd.read_csv(csv_path)
    urban_sound = urban_sound[urban_sound['fold'] == fold]
    urban_sound['amplitudes'] = urban_sound.apply(get_amplitudes, axis=1)
    return urban_sound


def get_amplitudes(row):
    fold = row['fold']
    slice_file_name = row['slice_file_name']
    dir = os.path.dirname(__file__)

    wav_path = os.path.join(dir, 'UrbanSound8K', 'formatted_audio', slice_file_name)
    sample_rate, amps = scipy.io.wavfile.read(wav_path)

    if amps.ndim is 2:
        amps_single = amps[:,0]
    else:
        amps_single = amps[0:]

    max_length = 384000
    length_to_pad = max_length - len(amps_single)
    if length_to_pad > 0:
        amps_single = np.concatenate((amps_single, np.zeros(length_to_pad)))
    return amps_single.tolist()

if (__name__ == "__main__"):
    main()
