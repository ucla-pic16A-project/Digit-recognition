from matplotlib import pyplot as plt
import sys
from sklearn import metrics
import numpy as np


class image_process:
    def __init__(self, df):
        self.df = df

    def show_image (self, n):
        '''
            returns an image of the nth element in dataset
        '''
        fig, ax = plt.subplots(1)
        img = self.df.iloc[n].values.reshape(28, 28)
        ax.imshow(img, cmap = plt.cm.binary)

    def show_nine_image (self, n):
        '''
            returns 9 images starting from the nth index in dataset on a 3x3 grid
        '''
        fig, ax = plt.subplots(3,3, figsize=(6,6))
        for i in range(3):
            for j in range (3):
                try:       
                    img = self.df.iloc[n+3*i+j].values.reshape(28,28)
                    ax[i][j].imshow(img, cmap = plt.cm.binary)
                except IndexError as e:
                    print('Too big! Not enought iamges.', file=sys.stderr)
                    return

    def confusion_matrix(y_train, predict):
        '''creats a confusion matrix for the dataset

        Args:
            y_train (_type_): _description_
            predict (_type_): model.predict(X_train)
        '''
        matrix = metrics.confusion_matrix(y_train, predict)

        plt.figure(figsize=(6,6))
        plt.imshow(matrix,cmap=plt.cm.Blues)
        plt.title("Confusion Matrix for MNIST Data")
        plt.xticks(np.arange(10))
        plt.yticks(np.arange(10))
        plt.ylabel('Actual Label')
        plt.xlabel('Predicted Label')
        plt.colorbar()
        width,height = matrix.shape
        for x in range(width):
            for y in range(height):
                plt.annotate(str(matrix[x][y]),xy=(y,x),horizontalalignment='center',verticalalignment='center')
        plt.show()