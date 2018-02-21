import collections
from sklearn import tree

Features = collections.namedtuple('Features', 'weight texture')
features = [
    Features(140, 0),
    Features(130, 0),
    Features(150, 1),
    Features(170, 1),
    Features(100, 1),
    Features(100, 0)
]
labels = ["Apple", "Apple", "Orange", "Orange", "Orange", "Apple"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([Features(160, 0)])
