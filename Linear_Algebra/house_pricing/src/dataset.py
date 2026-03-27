import pandas as pd
import os
import kagglehub
from typing import Iterator
from feature_scaling import Feature_scaling 
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', None)

class Dataset:
    def __init__(self, filePath : str):
        self.filePath = filePath

    #TODO: spara val_data
    def processDataFile(self, chunksize=10000): # Take rows in CSV file; generate list with raw data
        reader = pd.read_csv(self.filePath, chunksize=chunksize)
        
        for chunk in reader:
            BHK_RK_MAP = {"BHK" : 1, "RK" : 0}
            chunk["BHK_OR_RK"] = chunk["BHK_OR_RK"].map(BHK_RK_MAP)
            train_data, val_data = train_test_split(chunk, test_size=0.2, random_state=1)
            
            for houseData in self.getRawDataAsList(train_data):
                yield houseData

    def getEvaluationData(self, chunksize=10000):
        fs = Feature_scaling()
        reader = pd.read_csv(self.filePath, chunksize=chunksize)
        
        for chunk in reader:
            BHK_RK_MAP = {"BHK" : 1, "RK" : 0}
            chunk["BHK_OR_RK"] = chunk["BHK_OR_RK"].map(BHK_RK_MAP)
            train_data, val_data = train_test_split(chunk, test_size=0.2, random_state=1)
            for houseData in self.getRawDataAsList(val_data):
                x_val = fs.scaleData(houseData)
                y_val = houseData[11]
                yield x_val, y_val

    # Take in pandas dataframe
    # Returns list of raw data (str, int, float)
    def getRawDataAsList(self, data : pd.DataFrame) -> Iterator[list]:
        for _, row in data.iterrows():
            yield list(row)

    #TODO: yield data
    #      
    def getData(self) -> list[float]: # Returns list of processed data (float)
        numFeatureIndexes = [3, 5, 9, 10] # improvement: not use hardcoded indexes
        featureIndexes = [1, 2, 4, 6, 7]
        fs = Feature_scaling()

        # pass 1: fit (get mean, std)
        for rawData in self.processDataFile():
            numFeatures = [rawData[el] for el in numFeatureIndexes]
            fs.welfordAlgorithm(numFeatures)

        fs.updateStd()

        # pass 2: transform (scale numerical data)
        # to transform: x_train, x_val
        # for: train, analyze   data
        for rawData in self.processDataFile():
            numFeatures = [rawData[el] for el in numFeatureIndexes]
            #TODO: join together the lists
            scaledData = fs.scaleData(numFeatures)
            binData = [rawData[i] for i in featureIndexes]
            
            x_train = binData + scaledData 
            y_train = rawData[-1] # actual price
            print(x_train)
            print(y_train) #TODO: yield  y_train
            #processedData Order: bin, num

            yield x_train, y_train


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
    print(list(pd.read_csv(datasetPath)))

if __name__ == "__main__":
    main()
