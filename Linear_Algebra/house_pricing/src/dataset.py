import pandas as pd
import os
import kagglehub

pd.set_option('display.max_columns', None)

def dataset():
    path = kagglehub.dataset_download("anmolkumar/house-price-prediction-challenge")
    
    print("Path to dataset files:", path)


    # change dataset type for reading
    if isinstance(path, list):
        path = path[0]

    files = os.listdir(path)
    print("files: ", files)

    # dataset 
    datasetPath = os.path.join(path, 'train.csv')
    dataset = pd.read_csv(datasetPath)
    for i in range(3): 
        print(dataset.loc[i])

    print(dataset.loc[0:4]) 
dataset()
