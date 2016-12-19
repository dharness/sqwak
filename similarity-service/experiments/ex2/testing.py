import tensorflow as tf
import numpy as np
import os


# x_data = np.random.rand(100).astype(np.float32)
# y_data = x_data * 10 + 2

# W = tf.Variable(tf.zeros([1]))
# b = tf.Variable(tf.zeros([1]))
# y = W * x_data + b


# # Minimize the mean squared errors.
# loss = tf.reduce_mean(tf.square(y - y_data))
# optimizer = tf.train.GradientDescentOptimizer(0.1)
# train = optimizer.minimize(loss)

# # Before starting, initialize the variables.  We will 'run' this first.
# init = tf.global_variables_initializer()

# tf.histogram_summary("W", W)
# # Launch the graph.
# sess = tf.Session()
# sess.run(init)

# Fit the line.
# for step in range(500):
#     # sess.run(train)
#     print(step, sess.run(W), sess.run(b))


x = tf.Variable(0) 

y = tf.square(x)
summary_op = tf.summary.scalar("nool_hist", y)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

path = os.path.dirname(os.path.abspath(__file__)) + '/logs'
train_writer = tf.train.SummaryWriter(path, sess.graph)
merged = tf.summary.merge_all()

for step in range(5):
    assign_op = x.assign(step)
    sess.run(assign_op)
    output, summary = sess.run([y, merged])
    print(step, output)
    train_writer.add_summary(summary, step)
    #train_writer.add_summary(sess.run(summary_op), output)

