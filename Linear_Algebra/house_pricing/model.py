import numpy as np
import kagglehub
import os
from src.dataset import Dataset
from src.algorithm import Model

class OnlineTrainingPipeline():
    def __init__(self):
        path = kagglehub.dataset_download("anmolkumar/house-price-prediction-challenge")
        datasetPath = os.path.join(path, 'train.csv')
        self.dataset = Dataset(datasetPath)
        
    def setup(self):
        pass

def main():
    model = Model()

    dataPL = OnlineTrainingPipeline()
    dataPL.dataset.computeMeanAndStd()

    y_mean = dataPL.dataset.get_y_mean()
    sampleSize = dataPL.dataset.get_sample_size()

    model.set_bias(y_mean)
    model.set_sample_size(sampleSize) 

    X = np.array([x for x, y in dataPL.dataset.getData()]) 

    Y = np.array([y for x, y in dataPL.dataset.getData()]) 

 #   e = np.array([model.compute_error(x, y) for x, y in dataPL.dataset.getData()])

    predict = model.y_predict(X)
    
    e_vector = model.compute_error(X, Y)

    print(e_vector.size)

#   compError = model.compute_error(X[0], Y[0])
  #  print(compError)


# data representation:
## POSTED_BY:ownername
# UNDER_CONSTRUCTION:1/0
# RERA:Approved by real estate ? 1/0
# BHK_NO.:amount of rooms
# BHK_OR_RK:room-kitchen or not? 1/0
# SQUARE_FT:area
# READY_TO_MOVE:1/0
# RESALE:1/0
# ADRESS:STRING
# LONGITUDE:int
# LATITUDE:int
# TARGET:price

if __name__ == "__main__":
    main()
