"""
    This is the basic linear regression. It was done with 7qts of pride
"""
from bokeh.plotting import figure, show, output_file
import bokeh.layouts
import bokeh.models
import bokeh.models.widgets
from sklearn import linear_model
import numpy as np
import random
import utils
import inspect
from bunch import Bunch
from math import floor


def train(training_data):
    training_data_cutoff = int(floor(len(training_data) * .7))
    random.shuffle(training_data)

    x_data = []
    y_data = []
    for i, sample in enumerate(training_data):
        x_data.append(sample["amplitudes"])
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
        title='Ordinary Least Squares Linear Regression',
        description=__doc__,
        train=train
    )