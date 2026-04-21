import pandas as pd
import numpy as np 

class Analytics():
    def __init__(self, model):
        self.model = model
   
    # for graph plotting
    def prediction_data(self, name : str, split : str, x : list[float], y : float):
        y_pred = self.model.y_predict(x)
        residuals = y_pred - y

        return pd.DataFrame({
            "model": name,
            "split": split,
            "actual_price": y.flatten(),
            "predicted_price": y_pred.flatten(),
            "residual": residuals.flatten(),
            "squared_error": (residuals ** 2).flatten(),
            "absolute_error": np.abs(residuals).flatten(),
        })
    
    # for table plot
    def analytic_metric_data(self, name : str, split : str, x : list[float], y : float):
        y_pred = self.model.y_predict(x)
        residuals = y_pred - y

        mse = np.mean(residuals ** 2)
        rmse = np.sqrt(mse)
        mae = np.mean(np.abs(residuals))

        ss_res = np.sum(residuals ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r2 = 1 - (ss_res / ss_tot)

        return pd.DataFrame([
            {
                "model": name,
                "split": split,
                "MSE": mse,
                "RMSE": rmse,
                "MAE": mae,
                "R2": r2,
            }
        ])
