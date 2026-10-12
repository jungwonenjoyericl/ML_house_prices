from math import sqrt

#TODO: calculate mean + std
# write it out to json in /data/metadata

class Feature_scaling():
    def __init__(self):
        self.n = 0
        self.stdList = list(0.0 for _ in range(4))
        self.meanList = list(0.0 for _ in range(4))
        self.sqSum = list(0.0 for _ in range(4))
        self.y_sum = 0.0

    # scales the data in (x - mean) / std
    # returns a new list 
    def scaleData(self, singlePass : list) -> list[float]:
        std = self.stdList
        x_scaled = []

        for i, x in enumerate(singlePass):
            if std[i] != 0:
                x_scaled.append((x - self.meanList[i])/std[i])
            else:
                x_scaled.append(0.0)
                # std = 0

        return x_scaled
    
    # Calculate mean and variance with Welfords Algorithm
    # update list of mean values
    def welfordAlgorithm(self, singlePass):
        self.n += 1

        for i in range(len(singlePass)):
            x_n = singlePass[i]
            prev_mean = self.meanList[i]
            meanQuotient = (x_n - prev_mean)/self.n

            cur_mean = prev_mean + meanQuotient
            
            self.meanList[i] = cur_mean
            
            M = self.sqSum[i] + (x_n - prev_mean)*(x_n - cur_mean)
            self.sqSum[i] = M

    # return the calculated std
    def updateStd(self):
        if self.n > 1:
            std = [sqrt(el/(self.n - 1)) for el in self.sqSum]
            self.stdList = std
        else:
            raise ValueError("Need at least 2 data samples to compute Standard Deviation")
    
    # updates total sum of all house prices
    # needed for mean(y)
    def update_y_sum(self, house_price : float):
        self.y_sum += house_price
    
    # returns mean of y
    # use of start bias
    def get_y_mean(self) -> float:
        y_mean = self.y_sum / self.n
        return y_mean

# Test
def main():
    import dataset as ds
    dp = ds.datasetPath
    
    d = ds.Dataset(dp)
    binary_features = ["UNDER_CONSTRUCTION"]
    for data in d.processDataFile():
        print(data)
        
if __name__ == "__main__":
    main()
