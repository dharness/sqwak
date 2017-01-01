---
layout: default
title: "Experiment 1: Linear Regression"
---

# [](#header-1) Experiment 1

## [](#header-2) Linear Regression

Basic linear regression to predict ratings using 316 samples. 221 training samples (~70%) and 95 testing samples.
It was done using the mean squared error as the loss function. No pre-processing has been done on the data. Significant differences between actual and predicted ratings.
Uses database 2016_12_31__17_48_00.gz

Over 10 unique trials with data appearing in random orders, the average accuracy was **9.84%**

```python
def train(training_data):
    random.shuffle(training_data)

    x_data = []
    y_data = []
    for i, sample in enumerate(training_data):
        x_data.append(sample["amplitudes"])
        y_data.append(sample["rating"])

    reg = linear_model.LinearRegression()
    reg.fit(x_data[:150], y_data[:150])

    predicted = reg.predict(x_data[150:])
    actual = y_data[150:]
    return predicted, actual
```

{% include image.html src="assets/ex_1_fig_1.png" caption="Experiment 1: Predicted vs. Actual" %}