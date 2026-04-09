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

    def predict(self, x : list[float]) -> float:
        X = np.array([el for el in x])
        Xw = np.dot(X, self.w)
        y_pred = (Xw + self.b).item()
        return y_pred

def main():
    m = Model()
    m.predict([1,2,3,4,5,6,7,8,9])


# additional improvements on geographical info:
# * distance to center of city
# * distance to water
# * distance to public transport
# * distance to school




if __name__ == "__main__":
    main()
