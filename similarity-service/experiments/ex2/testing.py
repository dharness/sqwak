import numpy as np
import os
from pymongo import MongoClient
import tensorflow as tf


db = MongoClient()
results = db.sqwaks.sounds.find()
N = len(results[0]["amplitudes"])
x_data = []

for sample in results:
    x_data.append(sample["amplitudes"])

x_data = np.array(x_data)
print(x_data.shape)

y_data = x_data * 10 + 2

W = tf.Variable(tf.zeros([N]))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b


# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
init = tf.global_variables_initializer()

# Launch the graph.
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))