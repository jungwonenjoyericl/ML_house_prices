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

    def set_bias(self, x : float):
        self.b = x

    def set_sample_size(self, n : int):
        self.n = n

    def set_learningRate(self, alpha : float):
        self.learningRate = alpha

    def y_predict(self, x : list[float]) -> float:
        y_pred = np.empty((0, 1))
        for dataPoint in x:
            X = np.array([el for el in dataPoint])
            Xw = np.dot(X, self.w)
            cur_y_pred = (Xw + self.b)
            y_pred = np.vstack([y_pred, cur_y_pred])
        return y_pred

    def compute_error(self, x : list[float], y : float):
        e_vec = np.empty((0, 1))

        y_pred_vec = self.y_predict(x)
        
        for i in range(y_pred_vec.size):
            e = y_pred_vec[i] - y[i]
            e_vec = np.vstack([e_vec, e])

        return e_vec
        
    def compute_weight_gradients(self, x : list[float], y : float) -> list[float]:
        e = self.compute_error(x, y)

        xT = x.T 
        weightGradients = (2/self.n) * np.dot(xT, e)
        biasGradient = (2/self.n) * sum(e)
        return weightGradients, biasGradient

    def compute_bias_gradient(self, e : list[float]) -> float:
        gradient = (2/self.n) * sum(e)
        return gradient

    def update_weight(self):
        e = self.compute_error
        self.w = self.w - self.learningRate * self.compute_weight_gradients(x, )
        

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
