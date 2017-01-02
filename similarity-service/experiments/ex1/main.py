from bokeh.plotting import figure, show, output_file
import bokeh.layouts
import bokeh.models
import bokeh.models.widgets
from sklearn import linear_model
from pymongo import MongoClient
import numpy as np
from bokeh.resources import CDN
from bokeh.embed import file_html
import random
import warnings
import sys
import os
import utils
from bunch import Bunch
from math import floor

# Supress a harmless scipy warning
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

db = MongoClient()
results = list(db.sqwaks.sounds.find())
training_data_cutoff = int(floor(len(results)*.7))

def train(training_data):
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

def plot():
    trained_data = train(results)
    utils.plot(trained_data, title='Ordinary Least Squares Linear Regression')


def report():
    YAML_headers = '---\nlayout: default\ntitle: "Experiment 2: FFT"\n---'
    path = os.path.realpath(__file__ + '../../../../../docs/_experiments/')
    report = open(path + "/report.md", "w")
    html = plot2(False)
    report.write(YAML_headers + html)
    report.close()

def get_accuracy(num_iterations = 10):
    accuracy = 0
    for i in range(num_iterations):
        trained_data = train(results)
        predicted = trained_data.predicted
        actual = trained_data.actual

        accuracy += calculate_accuracy(predicted, actual)
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
