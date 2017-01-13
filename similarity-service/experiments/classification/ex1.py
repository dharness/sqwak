from pymongo import MongoClient
import pandas as pd
import random
import numpy as np
from sklearn import tree
from sklearn import svm 
from math import floor

db = MongoClient()

num_samples = 30
class_3_cursor = db.urban_sound.mfc_librosa_2.find({"classID": 0})
class_1_cursor = db.urban_sound.mfc_librosa_2.find({"classID": 3})

results = list(class_3_cursor) + list(class_1_cursor)
random.shuffle(results)

urban_sound = pd.DataFrame(results)

X = urban_sound["features"].values.tolist()
Y = urban_sound["classID"].values.tolist()
n = len(Y)

cutoff = int(floor(n * 0.7))

X_train = X[:cutoff]
Y_train = Y[:cutoff]
X_test = X[cutoff:]
Y_test = Y[cutoff:]


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)

predictions = clf.predict(X_test)

print(predictions)

count = (np.array(Y_test) == predictions).sum()
print(str((count/float(len(Y_test))) * 100.) + "%")





