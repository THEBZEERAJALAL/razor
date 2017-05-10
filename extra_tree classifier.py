from sklearn.tree import ExtraTreeClassifier
from sklearn.datasets import load_iris
iris = load_iris()
clf = ExtraTreeClassifier()
clf = clf.fit(iris.data, iris.target)
pred = clf.predict(iris.data[:1, :])
print(pred)
acc = clf.score(iris.data, iris.target)
print(acc)