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

Green pipeline screen:
![Снимок экрана 2024-04-20 в 19 02 11](https://github.com/johnneon/ml_ops_lab/assets/53760291/fadaa47b-9b67-4b4b-8dfe-343e46367c52)


ML final review in pipeline:
![Снимок экрана 2024-04-20 в 19 02 35](https://github.com/johnneon/ml_ops_lab/assets/53760291/9e64e39b-00da-40f7-9fe3-c0579b83f466)
