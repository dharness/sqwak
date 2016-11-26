from model import train
from DataSet import DataSets
from pymongo import MongoClient
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np


def main():
    client = MongoClient()
    db = client.sqwaks

    data = [ d["amplitudes"] for d in db.sounds.find({"label": "shmaw"}) ] 

    # mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    # make the mnist data a bit more general
    # mnist.test.samples = mnist.test.images
    percent_test = 70.
    sqwak = DataSets(data, percent_test)

    sqwak_sample_length = 540672
    sqwak_accuracy = train(sqwak, sqwak_sample_length)
    print(sqwak_accuracy)

    # mnist_sample_length = 784
    # mnist_accuracy = train(mnist, mnist_sample_length)
    # print(mnist_accuracy)

if (__name__ == "__main__"):
    main()