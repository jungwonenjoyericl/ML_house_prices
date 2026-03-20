import numpy as np
import pandas as pd
import os
import kagglehub

# Download latest version
path = kagglehub.dataset_download("anmolkumar/house-price-prediction-challenge")
print("Path to dataset files:", path)

if isinstance(path, list):
    path = path[0]

files = os.listdir(path)
print("files: ", files)


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
# y = w1x1 + w2x2 + w3x3 + w4x4 + ... + bi ||  , wi:weight x1:feature ie rooms/area/position bi: bias


# instructions
# geographical feature: coordinates
# additional improvements on geographical info:
# * distance to center of city
# * distance to water
# * distance to public transport
# * distance to school
# rest already have numerical representation
