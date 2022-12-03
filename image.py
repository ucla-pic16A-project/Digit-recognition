from matplotlib import pyplot as plt

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