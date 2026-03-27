import pandas as pd
import os
import kagglehub
from typing import Iterator
from feature_scaling import Feature_scaling 

pd.set_option('display.max_columns', None)

class Dataset:
    def __init__(self, filePath : str):
        self.filePath = filePath

    def processDataFile(self, chunksize=10000): # Take rows in CSV file; generate list with raw data
        reader = pd.read_csv(self.filePath, chunksize=chunksize)
         
        for chunk in reader:
            for houseData in self.getRawDataAsList(chunk):
                yield houseData

    # Take in pandas dataframe
    # Returns list of raw data (str, int, float)
    def getRawDataAsList(self, data : pd.DataFrame) -> Iterator[list]:
        for _, row in data.iterrows():
            yield list(row)


    #TODO: improve by using Welford's algorithm
    # Currently using two-pass (slower for bigger datasets)
    # pass 1: get mean
    # pass 2: get std
    # pass 3: stream scaled data
    # ^^ 2 passes when using Welford's algorithm
    def getData(self) -> list[float]: # Returns list of processed data (float)
        nonBinaryFeatureIndexes = [3, 5, 9, 10, 11] # improvement: not use hardcoded indexes
        fs = Feature_scaling()

        # ---- 
        for rawData in self.processDataFile():
            #TODO: Use dataparsing - Feature Scaling
            # scale
            # yield the updated list (same order as original)
            numericalFeatures = [rawData[el] for el in nonBinaryFeatureIndexes]
         #   fs.addData(numericalFeatures)

        #print(fs.mean()) # gets mean values

        #for rawData in self.processDataFile():
        #numericalFeatures = [rawData[el] for el in nonBinaryFeatureIndexes]

        #fs.stdStream(numericalFeatures)
        #print(fs.std())
        # ----
            fs.welfordAlgorithm(numericalFeatures)
        print(fs.getMean())
        print(fs.getStd())
        #TODO: scale data 
        for rawData in self.processDataFile():
          #  numFeatures = [rawData[el] for el in nonBinaryFeatureIndexes]
         #   scaledFeatures = fs.scaleData(numFeatures)
            #TODO: join together the lists
            pass 
# Get data
path = kagglehub.dataset_download("anmolkumar/house-price-prediction-challenge")
datasetPath = os.path.join(path, 'train.csv')

# Test
def main():
    d = Dataset(datasetPath)
    d.getData()
    #print((pd.read_csv(datasetPath)).shape)
    for houseData in d.processDataFile(): # This method to get generated objects
        #print(houseData)
        pass
if __name__ == "__main__":
    main()
