from pymongo import MongoClient
import pandas as pd
import random
import numpy as np
from sklearn import tree
from math import floor

db = MongoClient()

# fold_1_cursor = db.urban_sound.audio.find({"fold": 1}, {"amplitudes": 0}).skip(10).limit(10)
num_samples = 30
class_3_cursor = db.urban_sound.audio.find({"classID": 3}).skip(num_samples).limit(10)
class_1_cursor = db.urban_sound.audio.find({"classID": 1}).skip(num_samples).limit(10)

results = list(class_3_cursor) + list(class_1_cursor)
random.shuffle(results)

urban_sound = pd.DataFrame(results)

X = urban_sound["amplitudes"].values.tolist()
Y = urban_sound["classID"].values.tolist()
n = len(Y)

cutoff = int(floor(n * 0.7))

X_train = X[:cutoff]
Y_train = Y[:cutoff]
X_test = X[cutoff:]
Y_test = Y[cutoff:]


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)

predictions = clf.predict(X_test, Y_test)

count = (np.array(Y_test) == predictions).sum()
print str((count/float(n)) * 100.) + "%"





