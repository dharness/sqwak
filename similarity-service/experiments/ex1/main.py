"""
**Notes:**

This model is pretty terrible at rating sqwaks. Just look at that dismal accuracy score.
Also, note the position of the purple dots (where the prediction matches the actual rating). It seems to be good at knowing when a sqwak should receive a rating of 0!
This model seems to predict a rating that is consistently lower than the actual rating.

Stay tuned to see if we improve in [experiement 2!](2.html)

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
        x_data.append(sample["amplitudes"])
        y_data.append(sample["rating"])

    reg = linear_model.LinearRegression()
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
        title='Ordinary Least Squares Linear Regression',
        experiment_id="1",
        description=__doc__,
        train=train,
        processing_method="None",
        learning_alg="Ordinary Least Squares"
    )