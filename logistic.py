import numpy as np
from sklearn.model_selection import train_test_split

# To be honest, I think this class should be seperated into individual functions
class binary_logistic:
    def __init__(self, X, y):
        self.X = X
        self.y = y
    
    def gradient_descent_logistic(self, X, y, W0 = None, iter_times=100, stopping_diff=0.01):
        """ Binary logistic regression using gradient descent

        Args:
            X (p * n list like object): Sample data, for our usage is 2d array where each column is pixels for a number
            y (n * 1 list): Label for each number
            W0 (_type_, optional): Starting parameters. Defaults to None.
            iter_times (int, optional): Max number of iterations. Defaults to 100.
            stopping_diff (float, optional): Error to be considered as converged. Defaults to 0.01.

        Returns:
            list of floats: Fitted parameters
        """
        # If no starting parameters given, just choose randomly
        if W0 is None:
            W0 = np.random.rand(X.shape[0], 1)
        
        W1 = W0.copy()
        i = 0
        grad = np.ones(W0.shape)
        # while not converged or reached maximum iteration
        while (i < iter_times) and np.linalg.norm(grad) > stopping_diff:
            # @ is matrix multiplication
            Q = 1 / (1 + np.exp(-X.T @ W1))
            grad = X @ (Q - y)
            # The (np.log(i+1) / (((i+1) ** (0.5)))) thing is the hyperparameter
            # I have no idea why somehow this number is often chosen
            W1 = W1 - (np.log(i+1) / (((i+1) ** (0.5)))) * grad
            i = i + 1
        return W1
    
    def compute_accuracy(self, X_test, y_test, W, relation={0:0, 1:1}, threshold=0.5):
        """ Compute the accuracy of of trained paramters in test set

        Args:
            X_test (n * p matrix): Test set pixels
            y_test (n * 1 matrix): labels for test set
            W (list with length n): Fitted parameters
            relation (dict, optional): {x:0, y:1} if we would like to classify between number x and y . Defaults to {0:0, 1:1}.
            threshold (float, optional): Probability bigger than this threshold will be treated as 1. Defaults to 0.5.

        Returns:
            float: percentage of accurate prediction
        """
        count = 0
        for i in range(len(X_test)):
            predict = -1
            score = 0
            # This calculates the probability that the given image represent with label 0 
            # based on the fitted parameters
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
        """ Extract all data from dataset that related to number i and number j

        Args:
            i (int): First number
            j (int): Second number

        Returns:
            Dataframe, Dataframe: Pixels for all numbers with label i and j, Correponding labels
        """
        # Raise ValueError for incorrect numbers
        if not (0 <= i and i <= 9) or not (0 <= j and j <= 9):
            raise ValueError
        boolean_index = (self.y['class'] == i) | (self.y['class'] == j)
        return self.X[boolean_index], self.y[boolean_index]
    
    def train(self, i, j, testsize=0.3):
        """ Essentially a wrapper for the whole class

        Args:
            i (int): number to classify
            j (int): the other number to classify
            testsize (float, optional): Percentage for the test size. Defaults to 0.3.

        Returns:
            List[float], float: fitted parameters, percentage of correctness in test set
        """
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
        """ Wrapper for trying to classify between every pair of numbers

        Returns:
            List[List[float]], size: 10 * 10: Matrix with entry i, j represents the training score for classifying number i and j
        """
        result = np.reshape(np.arange(100, dtype=float), (10, 10))
        
        # Just compute halfway, the matrix should be symmetric
        for i in range(10):
            for j in range(i, 10):
                if i == j:
                    result[i,j] = 1
                else:
                    W, score = self.train(i, j)
                    result[i,j] = score
        
        # Flip the matrix to make it symmetric           
        for i in range(10):
            for j in range(10):
                if j >= i:
                    continue
                else:
                    result[i, j] = result[j, i]
                    
        # So that we don't have that many digits...
        return np.round(result, 4)
        