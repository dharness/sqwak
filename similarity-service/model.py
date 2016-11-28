import tensorflow as tf
import random


def train(buffered_audio):
    random.shuffle(buffered_audio)
    bit_length = len(buffered_audio[0])

    def next_batch():
        ys = [[0, 1]] * len(buffered_audio)
        return (buffered_audio[:70], ys[:70])

    def test_batch():
        ys = [[0, 1]] * len(buffered_audio)
        return (buffered_audio[70:100], ys[70:100])

    x = tf.placeholder(tf.float32, [None, bit_length])
    W = tf.Variable(tf.zeros([bit_length, 2]))
    b = tf.Variable(tf.zeros([2]))

    y = tf.nn.softmax(tf.matmul(x, W) + b)
    y_ = tf.placeholder(tf.float32, [None, 2])

    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)


    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)

    for i in range(1):
        batch_xs, batch_ys = next_batch()
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print(sess.run(accuracy, feed_dict={x: test_batch()[0], y_: test_batch()[1]}))

