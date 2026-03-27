from math import sqrt

#TODO: calculate mean + std
# write it out to json in /data/metadata

class Feature_scaling():
    def __init__(self):
        self.n = 0
        self.sums = list(0.0 for _ in range(5))  # can improve/vary    
        self.sqStd = self.sums
        self.meanList = self.sums
        self.sqSum = self.sums

    # scales the data in (x - mean) / std
    # returns a new list 
    def scaleData(self):
        #TODO: use calculated constants to scale data
        pass

    def welfordAlgorithm(self, singlePass):
        
        for i in range(len(singlePass)):
            self.n += 1
            x_n = singlePass[i]
            prev_mean = self.meanList[i]
            meanQuotient = (x_n - prev_mean)/self.n
            cur_mean = prev_mean + meanQuotient
            self.meanList[i] = cur_mean
            M = self.sqSum[i] + (x_n - prev_mean)*(x_n - cur_mean)
            self.sqSum[i] = M
            # TODO: fix ^^^


    def getStd(self) -> list[float]:
        std = [sqrt(el/(self.n - 1)) for el in self.sqSum]
        return

    def getMean(self) -> list[float]:
        return self.meanList

    # calculate a list with all mean values
    # return a calculated mean
    def mean(self) -> list[float]:
        mean = [el/self.n for el in self.sums]
        return mean
            
    # take list of one features values as input
    # return a calculated std
    def std(self) -> list[float]:
        std = [sqrt(el) for el in self.sqStd]
        return std
    
    # adds data to self.sums for every index
    # updates current sum of data, adds to meanLength(mathematically notated n)
    def addData(self, singlePass : list):
        #TODO: get a list with mean of all features in order
        for i in range(len(singlePass)):
            self.sums[i] += singlePass[i]
        self.n += 1

    # adds every term on iteration of sigma((xi - mean)**2)/n to std list
    def stdStream(self, singlePass : list):
        for i in range(len(singlePass)):
            x_i = singlePass[i]
            mean = self.mean()[i]

            numerator = (x_i - mean)**2
            quotient = numerator/self.n

            self.sqStd[i] += quotient

# Test
def main():
    import dataset as ds
    dp = ds.datasetPath
    
    d = ds.Dataset(dp)
    binary_features = ["UNDER_CONSTRUCTION"]
    for data in d.processDataFile():
        print(data)
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
