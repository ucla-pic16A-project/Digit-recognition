import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml

def read_from_openml():
    """ Get dataset from openml MNIST

    Returns:
        pandas dataframe containing pixels of numbers and thier labels
    """
    X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
    X = X / 255
    return X,y

def export_csv():
    """ Export the panda dataframe to .csv file so that 
        subsequent fetch data becomes faster
    """
    X,y = read_from_openml()
    # Store the file in the current working directory
    path_data = os.getcwd() + '/data.csv'
    path_result = os.getcwd() + '/result.csv'
    # Index equals False helps to eliminate the additional
    # index column when actually exporting to panda dataframe.
    X.to_csv(path_data, index=False)
    y.to_csv(path_result, index=False)

def read_from_csv():
    """ Read data from .csv file
        This only works if those csv files
        generated in the previous function stores in
        the current directory

    Returns:
        pandas dataframe containing pixels of numbers and thier labels
    """
    path_data = os.getcwd() + '/data.csv'
    path_result = os.getcwd() + '/result.csv'
    X = pd.read_csv(path_data)
    y = pd.read_csv(path_result)
    return X,y

def read_data():
    """ Read from csv if possible, else read from openml

    Returns:
        pandas dataframe containing pixels of numbers and thier labels
    """
    try:
        X, y = read_from_csv()
        return X,y
    except FileNotFoundError:
        export_csv()
    