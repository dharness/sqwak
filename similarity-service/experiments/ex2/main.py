from sklearn import linear_model
from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt
import random
import warnings
import sys
from utils import calculate_accuracy

# Supress a harmless scipy warning
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

db = MongoClient()
results = list(db.sqwaks.sounds.find())


def train(training_data):
    random.shuffle(training_data)

    x_data = []
    y_data = []
    for i, sample in enumerate(training_data):
        x_data.append(sample["amplitudes"])
        y_data.append(sample["rating"])

    reg = linear_model.BayesianRidge()
    reg.fit(x_data[:150], y_data[:150])

    predicted = reg.predict(x_data[150:])
    actual = y_data[150:]
    return predicted, actual

def main():

    predicted, actual = train(results)

    plt.plot(predicted, color='r', label='Prediction')
    plt.plot(actual, color='b', label='Actual')
    plt.xlabel('Sample #')
    plt.ylabel('Rating')
    plt.title('Linear Regression 1')
    plt.legend()

    plt.show()

def get_accuracy(num_iterations = 10):
    accuracy = 0
    for i in range(num_iterations):
        predicted, actual = train(results)
        accuracy += calculate_accuracy(predicted, actual)
    print accuracy/num_iterations
