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

    def getData(self) -> list[float]: # Returns list of processed data (float)
        for rawData in self.processDataFile():
            #TODO: Use dataparsing - Feature Scaling
            # method for scaling: update mean every iteration
            # categorize/slice lists to numerical features
            # convert text/str data into numerical/float||str
            # scale
            # then add them up (same order as original)
            
            fs = Feature_scaling()
            for i in range(len(rawData)):
                  fs.addData(rawdata[i], i)

            #yield 
        

# Get data
path = kagglehub.dataset_download("anmolkumar/house-price-prediction-challenge")
datasetPath = os.path.join(path, 'train.csv')

# Test
def main():
    d = Dataset(datasetPath)
    d.getData()
    for houseData in d.processDataFile(): # This method to get generated objects
        #print(houseData)
        pass
if __name__ == "__main__":
    main()
