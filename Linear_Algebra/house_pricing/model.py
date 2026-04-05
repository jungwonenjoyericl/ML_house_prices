import kagglehub
import os
from src.dataset import Dataset

def main():
    path = kagglehub.dataset_download("anmolkumar/house-price-prediction-challenge")
    datasetPath = os.path.join(path, 'train.csv')
    dStream = Dataset(datasetPath)
    
    for x, y in dStream.getData():
        print(x)
        print("propery price: " + str(y))


if __name__ == "__main__":
    main()
