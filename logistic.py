import numpy as np
from sklearn.model_selection import train_test_split

class binary_logistic:
    def __init__(self, X, y):
        self.X = X
        self.y = y
    
    def gradient_descent_logistic(self, X, y, W0 = None, iter_times=100, stopping_diff=0.01):
        if W0 is None:
            W0 = np.random.rand(X.shape[0], 1)
        
        W1 = W0.copy()
        i = 0
        grad = np.ones(W0.shape)
        while (i < iter_times) and np.linalg.norm(grad) > stopping_diff:
            Q = 1 / (1 + np.exp(-X.T @ W1))
            grad = X @ (Q - y)
            W1 = W1 - (np.log(i+1) / (((i+1) ** (0.5)))) * grad
            i = i + 1
        return W1
    
    def compute_accuracy(self, X_test, y_test, W, relation={0:0, 1:1}, threshold=0.5):
        count = 0
        for i in range(len(X_test)):
            predict = -1
            score = 0
            for j in range(len(X_test[0])):
                score += X_test[i,j] * W[j, 0]
            if score > threshold:
                predict = 1
            else:
                predict = 0
                
            if predict == relation[y_test[i][0]]:
                count += 1
        return count / len(y_test)
    
    def extract_two_numbers(self, i, j):
        if not (0 <= i and i <= 9) or not (0 <= j and j <= 9):
            return
        boolean_index = (self.y['class'] == i) | (self.y['class'] == j)
        return self.X[boolean_index], self.y[boolean_index]
    
    def train(self, i, j, testsize=0.3):
        X_i_j, y_i_j = self.extract_two_numbers(i, j)
        X_i_j_train, X_i_j_test, y_i_j_train, y_i_j_test = train_test_split(X_i_j, y_i_j, test_size = testsize)
        X_i_j_train_after = X_i_j_train.values
        y_train_after = y_i_j_train.values
        H_train = X_i_j_train_after.T
        if i != 0 or j != 1:
            for k in range(len(y_train_after)):
                if y_train_after[k,0] == i:
                    y_train_after[k,0] = 0
                else:
                    y_train_after[k,0] = 1
        W = self.gradient_descent_logistic(H_train, y_train_after)
        score = self.compute_accuracy(X_i_j_test.values, y_i_j_test.values, W, relation={i:0, j:1})
        return W, score
    
    def compute_all_accuracy(self):
        result = np.reshape(np.arange(100, dtype=float), (10, 10))
        for i in range(10):
            for j in range(i, 10):
                if i == j:
                    result[i,j] = 1
                else:
                    W, score = self.train(i, j)
                    result[i,j] = score
        for i in range(10):
            for j in range(10):
                if j >= i:
                    continue
                else:
                    result[i, j] = result[j, i]
        return np.round(result, 4)
        