# MLOps homework

## What it does

It is a little sample CT (Continuous training) pipeline.
Pipeline script runs already prepared python scripts one by one.
So, first we download data from Kaggle, then process it, prepare model and test it.

What I use for this app:
1. Dataset - [Price Prediction -Multiple Linear Regression](https://www.kaggle.com/datasets/erolmasimov/price-prediction-multiple-linear-regression/data)
2. [sklearn](https://scikit-learn.org/stable/index.html) - for process data and learning its `LinearRegression` model.

## How to start app

There are two ways to use this app, downloading data from kaggle, or not.

We have ready `train/train.csv` and `train/train.csv` datasets, if we run the app, data won't be downloaded from kaggle,
so you can skip `1. Kaggle API Token` step to start. But if you want to test entire program, you supposed to delete
the following train and test folders with data in them.

#### 1. Kaggle API Token
To start, you need to obtain a [Kaggle](https://www.kaggle.com/account/login) authentication token. To do this, you will need to:
- Log in to your Kaggle account.
- Go to the "Account" section on your profile page.
- Click "Create New API Token". This will lead to the download of the `kaggle.json` file.
- Put this file into the root of this project like:
```
/ml_ops_hm_1/
    ...
    model_testing.py
    pipline.sh
    kaggle.json <--
```


#### 2. Install dependencies
Run:
```bash
pip install -r requirements.txt
```

#### 3. Starting pipeline
We need to make `pipeline.sh` - "executable".
To do this, run the following command:
```bash
chmod u+x pipeline.sh
```

#### 4. Run
Just start app with `./pipeline.sh`
