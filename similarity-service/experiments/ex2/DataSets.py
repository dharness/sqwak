import numpy as np
from math import floor

"""
Represents an individual dataset which keeps track of its data in batches
"""
class DataSet():
    def __init__(self, x_data, y_data):
        #y_data = [ np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype="float32") for x in x_data ]
        #x_data = np.array(x_data)
        self._samples = np.array(x_data)
        self._labels = np.array(y_data)
        self._next_batch_head = 0
    
    @property
    def samples(self):
        return self._samples

    @property
    def labels(self):
        return self._labels

    def next_batch(self, batch_size):
        if (self._next_batch_head + batch_size <= len(self._samples)):
            batch_tail = self._next_batch_head + batch_size
            samples = self._samples[self._next_batch_head:batch_tail]
            labels = self._labels[self._next_batch_head:batch_tail]
            self._next_batch_head = batch_tail
            return samples, labels
        else:
            return None, None


"""
Mirrors the top level mnist object for retrieving data sets
"""
class DataSets():
    def __init__(self, x_data, percent_test = 50):
        train_set_size = int(floor((percent_test/100) * len(x_data)))
        self._train_set = DataSet(x_data[:train_set_size])
        self._test_set = DataSet(x_data[train_set_size:])

    @property
    def train(self):
        return self._train_set

    @property
    def test(self):
        return self._test_set