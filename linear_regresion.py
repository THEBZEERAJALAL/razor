"""
@created on: 19/04/17,
@author: Thebzeera V,
@version: v0.0.1

Description:

"""

import pickle
from sklearn.linear_model import LinearRegression as LinReg
from rztdl.utils.file import read_csv


class LogisticRegression(object):
    """
    @author: Thebzeera V
    Logistic Regression Class

    """
    def __init__(self, train_data, train_label):
        self.train_data = train_data
        self.train_label = train_label
        self.model = LinReg()
        self.model.fit(self.train_data, self.train_label)
        self.filename = '/home/thebzeera/PycharmProjects/logistic_regression/finalized_model.sav'
        pickle.dump(self.model, open(self.filename, 'wb'))


    def predict(self, test_data):
        """
        @author: Thebzeera V

        :param test_data: Test Data
        :return:Predictions
        """
        pickle.load(open(self.filename, 'rb'))
        pred = self.model.predict(test_data)
        return pred
if __name__ == '__main__':
    train_data, train_label, test_data, test_label = read_csv('iris_dataset.csv', split_ratio=[70, 0, 30],
                                                                                  delimiter=",",
                                                                                  output_label=True, randomize=True)
    object = LogisticRegression(train_data=train_data, train_label=train_label)
    object.predict(test_data)
