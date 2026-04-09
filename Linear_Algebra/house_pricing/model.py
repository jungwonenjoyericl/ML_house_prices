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
    path = kagglehub.dataset_download("anmolkumar/house-price-prediction-challenge")
    datasetPath = os.path.join(path, 'train.csv')
    dataset = Dataset(datasetPath)
    
    dataset.computeMeanAndStd()
    y_mean = dataset.get_y_mean()

    model = Model()
    model.set_bias(y_mean)
    model.compute_and_set_error([1,2,3,4,5,6,7,8,9], 23)

# data representation:
# POSTED_BY:ownername
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
