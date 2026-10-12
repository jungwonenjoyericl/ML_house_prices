# House Price Prediction — Linear Regression from Scratch

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)

A house-price prediction project implementing **multiple linear regression and batch gradient descent from scratch** using Python and NumPy.

The main goal of the project is to understand the basic mathematics and implementation behind a regression model rather than relying on a pre-built machine learning estimator.

## Technical Overview

The model predicts house prices using nine input features:

- Number of rooms
- Property area
- Longitude and latitude
- Construction status
- RERA approval
- Property type
- Ready-to-move status
- Resale status

The prediction model is:

```text
ŷ = Xw + b
```

where:

- `X` is the feature matrix
- `w` contains the learned feature weights
- `b` is the bias
- `ŷ` is the predicted house price

Model parameters are optimized using **batch gradient descent** with Mean Squared Error as the loss function.

```text
MSE = (1/n) Σ(ŷ - y)²

∇w = (2/n) Xᵀ(ŷ - y)

∂b = (2/n) Σ(ŷ - y)
```

## Implementation

The regression algorithm is implemented manually rather than using `sklearn.linear_model`.

The project includes:

- Multiple linear regression
- Batch gradient descent
- Manual gradient computation
- Mean Squared Error loss
- Fixed-epoch training
- Convergence-based training
- Feature standardization
- Streaming mean and variance calculation
- Train/validation splitting
- Regression metrics and diagnostic plots

`scikit-learn` is currently used for dataset splitting, while the regression model and optimization logic are implemented directly with NumPy.

## Data Pipeline

```text
Kaggle dataset
      |
      v
Read CSV in chunks
      |
      v
Encode binary/categorical features
      |
      v
Compute feature mean and standard deviation
      |
      v
Standardize numerical features
      |
      v
Build feature matrix X and target y
      |
      v
Batch gradient descent
      |
      v
Predictions and evaluation
```

Numerical feature statistics are calculated using **Welford's online algorithm**, which allows mean and variance to be computed incrementally without loading the entire dataset for that calculation.

Numerical features are standardized using:

```text
x_scaled = (x - mean) / std
```

## Training

Two training strategies are implemented.

### Fixed epochs

Runs gradient descent for a predefined number of iterations.

```python
model.epochs_train(X, y, 100)
```

### Convergence-based

Training continues until the change in MSE falls below a specified threshold or the maximum number of epochs is reached.

```python
model.convergence_train(X, y, threshold=0.001)
```

The model bias is initialized using the mean house price, while feature weights initially start at zero.

## Evaluation

The analytics module calculates standard regression metrics:

- **MSE** — Mean Squared Error
- **RMSE** — Root Mean Squared Error
- **MAE** — Mean Absolute Error
- **R²** — Coefficient of determination

The project also supports visualization of:

- Actual vs. predicted prices
- Residuals
- Error distributions
- Evaluation metrics

## Project Structure

```text
ML_house_prices/
├── requirements.txt
└── Linear_Algebra/
    └── house_pricing/
        ├── model.py
        └── src/
            ├── algorithm.py
            ├── dataset.py
            ├── feature_scaling.py
            ├── analytics.py
            └── plot.py
```

### Main components

| File | Responsibility |
|---|---|
| `model.py` | Training pipeline and application entry point |
| `algorithm.py` | Linear regression and gradient descent |
| `dataset.py` | Dataset loading, splitting and preprocessing |
| `feature_scaling.py` | Online statistics and feature standardization |
| `analytics.py` | Regression metrics and prediction analysis |
| `plot.py` | Model diagnostic visualizations |

## Dataset

The dataset is downloaded automatically through `kagglehub` from the **House Price Prediction Challenge** dataset.

```python
kagglehub.dataset_download(
    "anmolkumar/house-price-prediction-challenge"
)
```

## Running the Project

Clone the repository:

```bash
git clone https://github.com/jungwonenjoyericl/ML_house_prices.git
cd ML_house_prices
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the model:

```bash
cd Linear_Algebra/house_pricing
python model.py
```

## Current Status

The core regression and training pipeline is implemented.

The current version performs metric analysis on the training data. A complete streamed validation/evaluation pipeline is still under development, so reported training metrics should not be interpreted as final out-of-sample model performance.

## Purpose

This project was built to develop a deeper understanding of the mathematical and computational foundations of machine learning, including:

- Linear regression
- Loss functions
- Gradient-based optimization
- Vectorized linear algebra
- Feature scaling
- Online statistical algorithms
- Model evaluation
