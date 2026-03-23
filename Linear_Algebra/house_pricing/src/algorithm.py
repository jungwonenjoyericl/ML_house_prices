import numpy as np
import pandas as pd
import os
import kagglehub
#from ../plot import plot



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


print(dataset.iloc[5])


# Get a function with linear regression
# Arguments, weight w(int), features x(list[int]), bias b(int)
# retuns y from || --- 
# y = w1x1 + w2x2 + w3x3 + w4x4 + ... + bi ||  , wi:weight x1:feature ie rooms/area/position bi: bias
def y_func(w: int, x: list, b: int):
    y = 0
    for el in x:
        y += w * el

    y += b
    return y


def get_data(i: int, path: str):
    temporaryData = dataset.iloc[i]
    return temporaryData

def linear_regression(li : list, b : float) -> float: 
    pass    


def standardisation():
    pass


# instructions
# geographical feature: coordinates
# additional improvements on geographical info:
# * distance to center of city
# * distance to water
# * distance to public transport
# * distance to school
# rest already have numerical representation


# Plot function
# plot(data) | pandas list as input

