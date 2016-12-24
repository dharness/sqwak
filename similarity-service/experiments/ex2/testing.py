import numpy as np
import os
from pymongo import MongoClient
import tensorflow as tf


db = MongoClient()
results = db.sqwaks.sounds.find()
N = len(results[0]["amplitudes"])
L = results.count()
x_data = []
y_data = []
for sample in results:
    x_data.append(sample["amplitudes"])
    y_data.append([sample["rating"]])

x_data = np.array(x_data).astype(np.float32)
y_data = np.array(y_data)
#y_data = x_data * 10 + 2

W = tf.Variable(tf.zeros([N, 1]))
b = tf.Variable(tf.zeros([L]))
y = tf.reduce_sum(tf.matmul(x_data, W), reduction_indices=[1], keep_dims=True) + b


# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.3)
train = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
init = tf.global_variables_initializer()

# Launch the graph.
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in range(L):
    sess.run(train)
    if step % 20 == 0:
        print("step", step)
        print("the W", sess.run(W))
        print("the beee", sess.run(b))