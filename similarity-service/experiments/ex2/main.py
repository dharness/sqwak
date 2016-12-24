from model import train
from testing2 import train2
from DataSets import DataSet
from pymongo import MongoClient
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import time
import random


#mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

def main():
    # percent_test = 70.
    # mnist.test.samples = mnist.test.images
    # accuracy = train(mnist, 784)
    # print(accuracy)

    db = MongoClient()

    results = db.sqwaks.sounds.find()

    sqwak_length = len(results[0]["amplitudes"])
    num_sqwaks = results.count()


    x_data = []
    y_data = []

    for sample in results:
        x_data.append(sample["amplitudes"])
        y_data.append([sample["rating"]])
    
    data_set = DataSet(x_data, y_data)
    # percent_test = 0.
    # sqwak = DataSets(data, percent_test)
    # sample_length = 3.5 * 44100
    # accuracy = train(results)
    # print(accuracy)
    train2(data_set, sqwak_length, num_sqwaks)

if (__name__ == "__main__"):
    start = time.time()
    main()
    end = time.time()
    print('time elapsed (s): ', end - start)
