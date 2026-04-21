import matplotlib.pyplot as plt
import os

class Plot():
    def _data_path(self, filename):
        projectPath = os.path.dirname(os.path.dirname(__file__))
        return os.path.join(projectPath, "data", filename)

    def plot_graph(self, plotData):
        actual = plotData["actual_price"]
        predicted = plotData["predicted_price"]

        plt.figure(figsize=(8, 6))
        plt.scatter(actual, predicted, alpha=0.35, s=12)

        min_price = min(actual.min(), predicted.min())
        max_price = max(actual.quantile(0.99), predicted.quantile(0.99))
        plt.plot([min_price, max_price], [min_price, max_price], color="red")
        plt.xlim(min_price, max_price)
        plt.ylim(min_price, max_price)
        
        plt.xlabel("Actual price")
        plt.ylabel("Predicted price")
        plt.title("Predicted vs Actual Price")
        plt.tight_layout()
      
        plt.savefig(self._data_path("plot.png"))
        plt.close()

    def plot_residuals(self, plotData):
        predicted = plotData["predicted_price"]
        residual = plotData["residual"]

        plt.figure(figsize=(8, 6))
        plt.scatter(predicted, residual, alpha=0.35, s=12)
        plt.axhline(0, color="red")

        x_min = predicted.min()
        x_max = predicted.quantile(0.99)
        residual_limit = max(abs(residual.quantile(0.01)), abs(residual.quantile(0.99)))
        plt.xlim(x_min, x_max)
        plt.ylim(-residual_limit, residual_limit)

        plt.xlabel("Predicted price")
        plt.ylabel("Residual")
        plt.title("Residuals vs Predicted Price")
        plt.tight_layout()

        plt.savefig(self._data_path("residuals.png"))
        plt.close()

    def plot_error_distribution(self, plotData):
        residual = plotData["residual"]
        lower = residual.quantile(0.01)
        upper = residual.quantile(0.99)
        focused_residual = residual[(residual >= lower) & (residual <= upper)]

        plt.figure(figsize=(8, 6))
        plt.hist(focused_residual, bins=40)
        plt.axvline(0, color="red")

        plt.xlabel("Prediction error")
        plt.ylabel("Count")
        plt.title("Prediction Error Distribution")
        plt.tight_layout()

        plt.savefig(self._data_path("error_distribution.png"))
        plt.close()

    def plot_absolute_error_distribution(self, plotData):
        absolute_error = plotData["absolute_error"]
        upper = absolute_error.quantile(0.99)
        focused_absolute_error = absolute_error[absolute_error <= upper]

        plt.figure(figsize=(8, 6))
        plt.hist(focused_absolute_error, bins=40)

        plt.xlabel("Absolute error")
        plt.ylabel("Count")
        plt.title("Absolute Error Distribution")
        plt.tight_layout()

        plt.savefig(self._data_path("absolute_error_distribution.png"))
        plt.close()

    def plot_metrics_table(self, metricsData):
        fig, ax = plt.subplots(figsize=(8, 2))
        ax.axis("off")

        table = ax.table(
            cellText=metricsData.round(4).values,
            colLabels=metricsData.columns,
            loc="center"
        )

        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 1.5)

        plt.tight_layout()
        plt.savefig(self._data_path("metrics_table.png"))
        plt.close()

def main():
    
    plot(x,y)

    projectPath = os.getcwd()
    plotImagePath = os.path.join(projectPath, "data", "plot.png")
    plt.savefig(plotImagePath)

if __name__ == "__main__":
    main()
