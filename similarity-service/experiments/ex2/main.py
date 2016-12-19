from model import train
from DataSets import DataSets
from pymongo import MongoClient
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import time
import random


def main():

    client = MongoClient()
    db = client.sqwaks

    data = [
        d["amplitudes"] for d in db.sounds.find({"label": "shmiggity-shmaw"})
    ]
    random.shuffle(data)

    percent_test = 70.
    sqwak = DataSets(data, percent_test)
    sample_length = 3.5 * 44100
    accuracy = train(sqwak, sample_length)
    print(accuracy)

if (__name__ == "__main__"):
    start = time.time()
    main()
    end = time.time()
    print('time elapsed (s): ', end - start)
