#TODO: calculate mean + std
# write it out to json in /data/metadata

class Feature_scaling():
    def __init__(self):
        self.meanLength = 0
        self.mean = list([] for _ in range(7))      
        self.std = list()

    def scaleData(self):
        #TODO: use calculated constants to scale data
        pass

    # calculate a list with all mean values
    # return a copy of a calculated mean
    def calculateMean(self):
        sum = 0
        i = 0

        for el in range(len(self.mean)):
            sum += self.mean[i]
            i += 1

        mean = sum/i
        return mean
            
    # take list of one features values as input
    # return calculated std
    def calculateStd(self):
        pass
    
    # adds data to [pos] index of self.mean list
    # updates current sum of data, adds to meanLength(mathematically n)
    def addData(self, val : float, pos : int):
        #TODO: get a list with mean of all features in order
        print(self.mean, val)
        
        try:
            self.mean[pos] += val 
            self.meanLength += 1
        except:
            self.mean[pos].append(val)

    def std(self):
        #TODO: get a list with std of all fieatures in order
        pass


# Test
def main():
    import dataset as ds

    dp = ds.datasetPath
    
    d = ds.Dataset(dp)
    binary_features = ["UNDER_CONSTRUCTION"]
    for data in d.processDataFile():
        print(type(data[i]))

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
if __name__ == "__main__":
    main()
