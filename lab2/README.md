# MLOps homework 

## What it does

MLOPs Jenkins ready app. For using it, you need to install jenkins, and use Jenkinsfile as main pipeline.

What I use for this app:
1. Dataset - [Price Prediction -Multiple Linear Regression](https://www.kaggle.com/datasets/erolmasimov/price-prediction-multiple-linear-regression/data)
2. [sklearn](https://scikit-learn.org/stable/index.html) - for process data and learning its `LinearRegression` model.

## How to start app

See [lab1](../lab1).

#### Kaggle API Token
To start, you need to obtain a [Kaggle](https://www.kaggle.com/account/login) authentication token. To do this, you will need to:
- Log in to your Kaggle account.
- Go to the "Account" section on your profile page.
- Click "Create New API Token". This will lead to the download of the `kaggle.json` file.

Then you need to install kaggle file as `kaggle_secret` in jenkins credentials.
