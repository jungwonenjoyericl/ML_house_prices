import numpy as np
import kagglehub
import os
from src.dataset import Dataset
from src.algorithm import Model
from src.analytics import Analytics
from src.plot import Plot

class OnlineTrainingPipeline():
    def __init__(self):
        path = kagglehub.dataset_download("anmolkumar/house-price-prediction-challenge")
        datasetPath = os.path.join(path, 'train.csv')
        self.dataset = Dataset(datasetPath)
        self.model = Model()
        
    def setup(self):
        self.dataset.computeMeanAndStd()
        
        y_mean = self.dataset.get_y_mean()
        n = self.dataset.get_sample_size()

        self.model.set_bias(y_mean)
        self.model.set_sample_size(n)
    
    def get_train_data(self):
        X, Y = zip(*self.dataset.getData())
        X = np.array(X)
        Y = np.array(Y).reshape(-1, 1)
        return X, Y

    def epochs_train(self, n : int):
        X, Y = self.get_train_data()
        self.model.epochs_train(X, Y, n)
        
    def convergence_train(self, threshold : float):
        X, Y = self.get_train_data()
        self.model.convergence_train(X, Y, threshold)

    def get_model_object(self):
        return self.model

def main():
    
    # Using batch gradient descent


    # Model A: trained with fixed epochs
    epoch_model_agent = OnlineTrainingPipeline()
    epoch_model_agent.setup()

    epochs = 100
    epoch_model_agent.epochs_train(epochs)

     
    # Model B: trained until convergence
    convergence_model_agent = OnlineTrainingPipeline()
    convergence_model_agent.setup()
    
    threshold = 0.001
    convergence_model_agent.convergence_train(threshold)

    X, Y = epoch_model_agent.get_train_data()
    analytics = Analytics(epoch_model_agent.get_model_object())

    graph_data = (analytics.prediction_data("Epoch 100", "TRAIN", X, Y))

    table_data = analytics.analytic_metric_data("Epoch 100", "TRAIN", X, Y)

    plot = Plot()
    plot.plot_graph(graph_data)
    plot.plot_residuals(graph_data)
    plot.plot_error_distribution(graph_data)
    plot.plot_metrics_table(table_data)

# data representation:
## POSTED_BY:ownername
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
