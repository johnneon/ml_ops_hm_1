from sklearn.model_selection import train_test_split

import pandas as pd

import os
# Setting up env var KAGGLE_CONFIG_DIR
os.environ['KAGGLE_CONFIG_DIR'] = '.'

# Then we can import kaggle api
from kaggle.api.kaggle_api_extended import KaggleApi


if __name__ == '__main__':
    train_full_path = './train/train.csv'
    test_full_path = './test/test.csv'

    # If data already exists, no need to download new
    if os.path.isfile(train_full_path) and os.path.isfile(test_full_path):
        print('Train and test data already exists.')
        print('Delete existing file if you wish to download new.')
        exit()

    # Create folders for data
    os.makedirs('train', exist_ok=True)
    os.makedirs('test', exist_ok=True)

    # Connect to api
    api = KaggleApi()
    api.authenticate()

    # Download dataset
    api.dataset_download_files(
        'erolmasimov/price-prediction-multiple-linear-regression',
        path='.',
        unzip=True
    )

    # Split it into train/test
    dataset_filename = './scrap price.csv'
    df = pd.read_csv(dataset_filename)
    train, test = train_test_split(df, test_size=.30, random_state=42)

    # Save datasets
    train.to_csv(train_full_path, index=False)
    test.to_csv(test_full_path, index=False)

    # Remove useless file
    if os.path.isfile(dataset_filename):
        os.remove(dataset_filename)

    print('Data successfully created.')
