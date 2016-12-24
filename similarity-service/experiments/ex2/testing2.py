import numpy as np
import os
from pymongo import MongoClient
import tensorflow as tf

# db = MongoClient()
# results = db.sqwaks.sounds.find()
logs_path = os.path.realpath(__file__) + "/../logs"

def train2 (data_set, N, L):

    # N = len(results[0]["amplitudes"])
    # L = results.count()

    x_data = []
    y_data = []

    # for sample in results:
    #     x_data.append(sample["amplitudes"])
    #     y_data.append([sample["rating"]])

    # x_data = np.array(x_data).astype(np.float32)
    # y_data = np.array(y_data)

    # create variables
    x = tf.placeholder(tf.float32, [None, N])
    W = tf.Variable(tf.zeros([N, 1]))
    b = tf.Variable(tf.zeros([10,1]))
    y = tf.matmul(x, W) + b
    y_ = tf.placeholder(tf.float32, [None, 1])

    # Set up some summaries
    w_h = tf.histogram_summary("weights", W)


    # Minimize the mean squared errors.
    loss = tf.reduce_mean(tf.square(y - y_))
    optimizer = tf.train.GradientDescentOptimizer(0.09)
    train = optimizer.minimize(loss)
    tf.summary.scalar('loss', loss)

    # Before starting, initialize the variables.  We will 'run' this first.
    init = tf.global_variables_initializer()

    # Launch the graph.
    sess = tf.Session()
    sess.run(init)

    merged = tf.summary.merge_all()
    summary_writer = tf.train.SummaryWriter(logs_path, sess.graph)

    for i in range(21):
        x_data, y_data = data_set.next_batch(10)
        s, train_result = sess.run([merged, train], feed_dict={x: x_data, y_: y_data})
        summary_writer.add_summary(s, i)



    print(sess.run(W))
    print('-------------------------------------------------------------------')
    print(sess.run(b))
    print('-------------------------------------------------------------------')
    yf = sess.run(y, feed_dict={x: x_data})
    print(yf)
    print(yf.shape)
    lossf = sess.run(loss, feed_dict={y: yf, y_: y_data})
    print('-------------------------------------------------------------------')
    print(lossf)