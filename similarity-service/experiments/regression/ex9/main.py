"""
**Notes:**

Demonstrates the same problem as using [ridge wth fft](11.html). These predictions are on an even straighter line than with ridge.
There seems to be no point in continuing with these methods till the database is filled with more sqwaks with low ratings.


"""
from sklearn import linear_model
import numpy as np
import random
import utils
import inspect
from bunch import Bunch
from math import floor


def train(training_data):
    # 70% of sqwaks for training, 30% for testing
    training_data_cutoff = int(floor(len(training_data) * .7))
    random.shuffle(training_data)

    x_data = []
    y_data = []
    for i, sample in enumerate(training_data):
        n = len(sample["amplitudes"])
        X = np.fft.fft(sample["amplitudes"])/n

        #  the magnitude sqrt(re^2 + im^2) tells you the amplitude of
        # the component at the corresponding frequency. 
        fft_amps = X[range(n/2)]
        im = np.imag(fft_amps)
        re = np.real(fft_amps)
        X = np.sqrt((im ** 2) + (re ** 2))

        x_data.append(X)
        y_data.append(sample["rating"])

    reg = linear_model.Lasso(alpha=0.001)
    reg.fit(x_data[:training_data_cutoff], y_data[:training_data_cutoff])

    # predict on the remaining 30%
    predicted = reg.predict(x_data[training_data_cutoff:])

    actual = y_data[training_data_cutoff:]
    
    return Bunch({
        "predicted": predicted, 
        "actual": actual,
        "x_data_test": x_data[training_data_cutoff:],
        "y_data_test": y_data[training_data_cutoff:],
        "reg": reg
    })

def report():
    results = utils.load_data()
    trained_data = train(results)
    utils.generate_report(
        trained_data,
        original_data=results,
        title='Lasso Regression of FFT',
        experiment_id="9",
        experiment_type="regression",
        description=__doc__,
        train=train,
        processing_method="FFT",
        learning_alg="Lasso",
        num_iterations=10
    )