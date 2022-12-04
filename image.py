from matplotlib import pyplot as plt
import sys

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
        fig, ax = plt.subplots(3,3, figsize=(8,8))
        for i in range(3):
            for j in range (3):
                try:       
                    img = self.df.iloc[n+3*i+j].values.reshape(28,28)
                    ax[i][j].imshow(img, cmap = plt.cm.binary)
                except IndexError as e:
                    print('Too big! Not enought iamges.', file=sys.stderr)
                    return