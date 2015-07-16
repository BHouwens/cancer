import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from data import Data

nice_data = Data()

clf = RandomForestClassifier()
clf.fit(nice_data.feature_train, nice_data.labels_train)

pred = clf.predict(nice_data.feature_test)
print accuracy_score(nice_data.labels_test, pred)