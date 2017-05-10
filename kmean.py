from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

x = [1, 2, 3.5, 6.5, 2, 3]
y = [5, 6, 9, 6, 6.9, 8.5]

plt.scatter(x, y)
# plt.interactive(False)
plt.show(block=True)
kmeans = KMeans(n_clusters=3, random_state=0).fit(x)
plt.show(kmeans)
