"""
**Notes:**

Here we preprocessed the amplitudes with the fast fourier transform.
The FFT produces complex numbers. We tested using the real only, imaginary only, phase, and magnitudes
of the FFT. The magnitude proved to consistently have the highest accuracy, so that is what is displayed here.

The FFT improved the accuracy quite a bit! Let's see how we do with the mel-frequency cepstrum in [experiment 3.](3.html)
"""
from sklearn import linear_model
import numpy as np
import random
import utils
from bunch import Bunch
from math import floor, sqrt, atan2
import pdb


def train(training_data):
    training_data_cutoff = int(floor(len(training_data) * .7))
    random.shuffle(training_data)

    x_data = []
    y_data = []

    for i, sample in enumerate(training_data):
        n = len(sample["amplitudes"])
        X = np.fft.fft(sample["amplitudes"])/n

        #  the magnitude sqrt(re^2 + im^2) tells you the amplitude of the component at the corresponding frequency. 
        fft_amps = X[range(n/2)]
        im = np.imag(fft_amps)
        re = np.real(fft_amps)
        X = np.sqrt((im ** 2) + (re ** 2))

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

def report():
    results = utils.load_data()
    trained_data = train(results)
    utils.generate_report(
        trained_data,
        original_data=results,
        title='Ordinary Least Squares Linear Regression of FFT',
        experiment_id="2",
        description=__doc__,
        train=train,
        processing_method="FFT",
        learning_alg="Ordinary Least Squares",
        num_iterations=10
    )
