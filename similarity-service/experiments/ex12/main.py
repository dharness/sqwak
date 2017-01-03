"""
Bayesian Regression MFC
"""
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import random
import utils
from bunch import Bunch
from math import floor

def train(training_data):
    # 70% of sqwaks for training, 30% for testing
    training_data_cutoff = int(floor(len(training_data) * .7))
    random.shuffle(training_data)

    x_data = []
    y_data = []

    sample_rate = 44100

    for i, sample in enumerate(training_data):
        # Preprocessing with mel-frequency cepstrum
        mfc_data = utils.mfc(np.asarray(sample["amplitudes"]), sample_rate)
        x_data.append(mfc_data)
        y_data.append(sample["rating"])

    reg = linear_model.BayesianRidge()
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
        title='Bayesian Regression MFC',
        experiment_id="12",
        description=__doc__,
        train=train,
        processing_method="MFC",
        learning_alg="Bayesian Regression",
        num_iterations=10
    )