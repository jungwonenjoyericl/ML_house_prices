import numpy as np
import pandas as pd
import os
import kagglehub
#from ../plot import plot



# Arguments, weight w(float), features x(list[float]), bias b(float)
# retuns y from || --- 
# y = w1x1 + w2x2 + w3x3 + w4x4 + ... + bi ||  , wi:weight x1:feature ie rooms/area/position bi: bias

class Model():
    def __init__(self):
        self.w : list[float] = np.array([[0.0] for _ in range(9)])
        self.b : int = 0 #TODO: change to mean(y_train)
        self.n : int = 0.0
        self.learningRate : float = 0.01
        self.prev_mse : float = 0.0

    def set_bias(self, x : float):
        self.b = x

    def set_sample_size(self, n : int):
        self.n = n

    def set_learningRate(self, alpha : float):
        self.learningRate = alpha

    #TODO: let this func handle loop, or the training func()
    def mean_squared_error(self, x : list[float], y : float):
        e = self.y_predict(x) - y
        return np.mean(e ** 2)
    
    # Calculates y_pred with current f(x) = Xw + b
    def y_predict(self, x : list[float]) -> float:
        y_pred = np.matmul(x, self.w) + self.b
        return y_pred

    # Calculates error from y_pred - y_val
    def compute_error(self, x : list[float], y : list[float]):
        y_pred_vec = self.y_predict(x)

        e_vec = y_pred_vec - y
        return e_vec
        
    # Computes gradients for weight and bias
    def compute_gradients(self, x : list[float], y : float) -> list[float]:
        e = self.compute_error(x, y)

        xT = x.T 
        n = x.shape[0]
        weightGradients = (2 / n) * np.dot(xT, e)
        biasGradient = (2 / n) * np.sum(e)
        return weightGradients, biasGradient
    
    # Updates the models parameter
    def update_parameters(self, x : list[float], y : float):
        w_gradient, b_gradient = self.compute_gradients(x, y)
        self.w = self.w - self.learningRate * w_gradient
        self.b = self.b - self.learningRate * b_gradient

    # set manual amount of iterations/loops
    def epochs_train(self, x : list[float], y : list[float], n : int):
        for epoch in range(1, n + 1):
            self.update_parameters(x, y)

    # loop til residual difference hits threshold
    def convergence_train(self, x : list[float], y : list[float], bound : float, max_epochs=10000):
        prev_mse = float("inf")

        for epoch in range(1, max_epochs + 1):
            self.update_parameters(x, y)

            cur_mse = self.mean_squared_error(x, y)
            
            if abs(prev_mse - cur_mse) < bound:
                break

            prev_mse = cur_mse

def main():
    m = Model()
    m.set_bias(142.3)
    print(m.predict([1,2,3,4,5,6,7,8,9]))
    m.compute_and_set_error([1,2,3,4,5,6,7,8,9], 112.2)
    print(m.e)

# additional improvements on geographical info:
# * distance to center of city
# * distance to water
# * distance to public transport
# * distance to school




if __name__ == "__main__":
    main()
