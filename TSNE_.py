import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from rztdl.utils.file import read_csv

class tSNE(object):
    """
    @author: Thebzeera V
    t-SNE Class

    """
    def __init__(self, n_iter, n_learning_rate, data, label):
        """
        :param n_component: number of dimension
        :param n_learning_rate: learning_rate
        """
        self.data = data
        self.label = label
        self.n_iter = n_iter
        self.learning_rate = n_learning_rate
        self.X_tsne = TSNE(n_iter=self.n_iter, learning_rate=self.learning_rate).fit_transform(self.data)

    def plot(self, name='t-SNE', xlabel='', ylabel='', save_path=None, show=True):
        """
        :param name: name of the graph
        :param xlabel: xlabel
        :param ylabel: ylabel
        :param save_path: save path
        :param show: show

        """
        plt.scatter(self.X_tsne[:, 0], self. X_tsne[:, 1], c=self.label)
        plt.title(name)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        if save_path:
            plt.savefig(save_path)
        if show:
            plt.show()
        return self

if __name__ == '__main__':
    data, label = read_csv('sum.csv', split_ratio=[100, 0, 0], delimiter=",",
                                                              output_label=True, randomize=True)
    obj_tSNE = tSNE(n_iter=500, n_learning_rate=200, data=data, label=label)
    obj_tSNE.plot()
