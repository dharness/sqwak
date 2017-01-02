"""
    This is the basic linear regression. It was done with 7qts of pride
"""
from sklearn import linear_model
import numpy as np
import random
import utils
import inspect
from bunch import Bunch
from math import floor


# Supress a harmless scipy warning
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

db = MongoClient()
results = list(db.sqwaks.sounds.find())
training_data_cutoff = int(floor(len(results) * .7))


def train(training_data):
    random.shuffle(training_data)

    x_data = []
    y_data = []
    for i, sample in enumerate(training_data):
        n = len(sample["amplitudes"])
        X = np.fft.fft(sample["amplitudes"])/n
        X = X[range(n/2)]
        x_data.append(X)
        y_data.append(sample["rating"])

    reg = linear_model.LinearRegression()
    reg.fit(x_data[:training_data_cutoff], y_data[:training_data_cutoff])


    predicted = reg.predict(x_data[training_data_cutoff:])
    actual = y_data[training_data_cutoff:]
    
    return Bunch({
        "predicted": predicted, 
        "actual": actual,
        "x_data_test": x_data[training_data_cutoff:],
        "y_data_test": y_data[training_data_cutoff:],
        "reg": reg
    })

def plot():
    trained_data = train(results)
    utils.plot(trained_data)


def get_accuracy(num_iterations = 10):
    accuracy = 0
    for i in range(num_iterations):
        trained_data = train(results)
        predicted = trained_data.predicted
        actual = trained_data.actual

        accuracy += utils.calculate_accuracy(predicted, actual)
    print accuracy/num_iterations

def mean_sqr_err():
    trained_data = train(results)
    predicted = trained_data.predicted
    actual = trained_data.actual
    reg = trained_data.reg
    
    x_data_test = trained_data.x_data_test
    y_data_test = trained_data.y_data_test
    
    print("Mean s quared error: %.2f"
      % np.mean((predicted - actual) ** 2))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % reg.score(x_data_test, y_data_test))

def plot_fft():
    x_data = results[100]["amplitudes"]
    n = len(x_data)
    Y = np.fft.fft(x_data)/n
    Y = Y[range(n/2)]

    plt.plot(Y, color='r', label='Prediction')
    plt.xlabel('time')
    plt.ylabel('FFT')
    plt.title('FFT of a sqwak')
    plt.legend()

    plt.show()
