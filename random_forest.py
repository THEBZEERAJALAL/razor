# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import cross_val_score
# X = [[0, 0], [1, 1]]
# Y = [0, 1]
# clf = RandomForestClassifier(n_estimators=10)
# clf = clf.fit(X, Y)
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
iris = load_iris()
clf = RandomForestClassifier()
clf = clf.fit(iris.data, iris.target)
pred = clf.predict(iris.data[:1, :])
print(pred)