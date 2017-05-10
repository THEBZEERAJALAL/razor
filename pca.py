from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from rztdl.utils.file import read_csv

class Pca(object):
    """
    @author: Thebzeera V
    PCA Class

    """
    def __init__(self, n_component, data, label):
        """
        :param n_component: number of dimension
        """
        self.data = data
        self.label = label
        self.n_componet = n_component
        self.X_pca = PCA(n_components=self.n_componet).fit_transform(self.data)

    def plot(self, name='pca', xlabel='', ylabel='', save_path=None, show=False):
        """

        :param name: name of the graph
        :param xlabel: xlabel
        :param ylabel: ylabel
        :param save_path: save path
        :param show: show

        """
        plt.scatter(self.X_pca[:, 0], self.X_pca[:, 1], c=self.label)
        plt.title(name)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        if save_path:
            plt.savefig(save_path)
        if show:
            plt.show()
        return self

if __name__ == '__main__':
    data, label = read_csv('iris_dataset.csv', split_ratio=[100, 0, 0], delimiter=",", output_label=True, randomize=True)
    obj_Pca = Pca(n_component=4, data=data, label=label)
    obj_Pca.plot(name='PCA', save_path=None, show=True)