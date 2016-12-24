import tensorflow as tf
import os

def train(data_set, sample_length):
    logs_path = os.path.realpath(__file__) + "/../logs"

    x = tf.placeholder(tf.float32, [None, sample_length])
    W = tf.Variable(tf.zeros([sample_length, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    y_ = tf.placeholder(tf.float32, [None, 10])

    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    
    tf.summary.scalar('cross_entropy', cross_entropy)
    merged = tf.summary.merge_all()
    summary_writer = tf.train.SummaryWriter(logs_path, sess.graph)


    for i in range(1000):
        batch_xs, batch_ys = data_set.train.next_batch(100)
        s, train_result = sess.run([merged, train_step], feed_dict={x: batch_xs, y_: batch_ys})
        summary_writer.add_summary(s, i)

    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={x: data_set.test.samples, y_: data_set.test.labels})

    return result