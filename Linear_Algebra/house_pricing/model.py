import kagglehub
import os
from src.dataset import Dataset

def main():
    path = kagglehub.dataset_download("anmolkumar/house-price-prediction-challenge")
    datasetPath = os.path.join(path, 'train.csv')
    dStream = Dataset(datasetPath)
    

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



    for x, y in dStream.getData():
        print(x)
        print("propery price: " + str(y))


if __name__ == "__main__":
    main()
