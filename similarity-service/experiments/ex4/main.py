"""
Stochastic Gradient Descent
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
        x_data.append(sample["amplitudes"])
        y_data.append(sample["rating"])
    
    reg = linear_model.SGDRegressor()
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
        title='Stochastic Gradient Descent',
        experiment_id="4",
        description=__doc__,
        train=train,
        processing_method="None",
        learning_alg="Stochastic Gradient Descent",
        num_iterations=10
    )
