from model import train
from DataSets import DataSets
from pymongo import MongoClient
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import time
import random

# from process_audio import get_buffered_amplitudes


def main():

    client = MongoClient()
    db = client.sqwaks

    data = [
        d["amplitudes"] for d in db.sounds.find({
            "label": "shmiggity-shmaw"
        })
    ]
    random.shuffle(data)

    percent_test = 70.
    sqwak = DataSets(data, percent_test)
    sample_length = 3.5 * 44100
    accuracy = train(sqwak, sample_length)
    print(accuracy)

    # mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    # make the mnist data a bit more general
    # mnist.test.samples = mnist.test.images
    # percent_test = 70.
    # sqwak = DataSets(data, percent_test)
    # old_sqwak = DataSets(old_data, percent_test)

    # old_sqwak_sample_length = 180224
    # old_sqwak_accuracy = train(old_sqwak, old_sqwak_sample_length)
    # print(old_sqwak_accuracy)

    # sqwak_sample_length = 540672
    # sqwak_accuracy = train(sqwak, sqwak_sample_length)
    # print(sqwak_accuracy)

    # mnist_sample_length = 784
    # mnist_accuracy = train(mnist, mnist_sample_length)
    # print(mnist_accuracy)


if (__name__ == "__main__"):
    start = time.time()
    main()
    end = time.time()
    print('time elapsed (s): ', end - start)
