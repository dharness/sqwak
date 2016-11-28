from pymongo import MongoClient
from process_audio import get_buffered_amplitudes


def upload():
    db = MongoClient()

    amps = get_buffered_amplitudes("./output.wav")
    result = db.sqwaks.test.insert_one({
        "amplitudes": amps[0]
    })
    print(result)


if(__name__ == "__main__"):
    upload()