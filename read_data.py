import os
import pandas as pd
from sklearn.datasets import fetch_openml

def read_from_openml():
    X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
    X = X / 255
    return X,y

def export_csv():
    X,y = read_from_openml()
    path_data = os.getcwd() + '/data.csv'
    path_result = os.getcwd() + '/result.csv'
    X.to_csv(path_data, index=False)
    y.to_csv(path_result, index=False)

def read_from_csv():
    path_data = os.getcwd() + '/data.csv'
    path_result = os.getcwd() + '/result.csv'
    X = pd.read_csv(path_data)
    y = pd.read_csv(path_result)
    return X,y
    