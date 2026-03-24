import pandas as pd
import os
import kagglehub

pd.set_option('display.max_columns', None)

class dataset:
    def __init__(self, df : pd.DataFrame): # (self, link : str, dataPath : str)
        self.dataset = df
        #for now take in dataframe as argument 
    

    #TODO: scale better, optimize function for bigger data
    def getRawDataAsList(self) -> list: # Returns list of raw data (str, int, float)
        testCap = 0

        for index, row in self.dataset.iterrows():
            if testCap > 4:
                return
            testCap += 1
            
            print(list(row))
            yield list(row)

    def getData() -> list[float]: # Returns list of processed data (float)
        for houseData in d.getRawDataAsList():
            #TODO: Use dataparsing - Feature Scaling
            pass 

            #yield 
        

# Get data
path = kagglehub.dataset_download("anmolkumar/house-price-prediction-challenge")
datasetPath = os.path.join(path, 'train.csv')
DATA = pd.read_csv(datasetPath)

# Test
d = dataset(DATA)
for houseData in d.getRawDataAsList(): # This method to get generated objects
    print(houseData)
