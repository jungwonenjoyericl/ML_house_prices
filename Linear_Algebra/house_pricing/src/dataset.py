import pandas as pd
import os
import kagglehub

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

    def getData() -> list[float]: # Returns list of processed data (float)
        for rawData in self.processDataFile():
            #TODO: Use dataparsing - Feature Scaling
        
            pass

            #yield 
        

# Get data
path = kagglehub.dataset_download("anmolkumar/house-price-prediction-challenge")
datasetPath = os.path.join(path, 'train.csv')

# Test
def main():
    d = Dataset(datasetPath)
    for houseData in d.processDataFile(): # This method to get generated objects
        print(houseData)

if __name__ == "__main__":
    main()
