import os

import pandas as pd

import pickle

from sklearn.model_selection import cross_validate
from sklearn.model_selection import ShuffleSplit

scoring_reg = {'R2': 'r2',
               '-MSE': 'neg_mean_squared_error',
               '-MAE': 'neg_mean_absolute_error',
               '-Max': 'max_error'}

cv_rule = ShuffleSplit(n_splits=5, random_state=42)


def cross_validation(X, y, model, scoring, cv_rule):
    """
    Calculation of metrics on cross-validation.
    Parameters:
        - model: model or pipeline
        - X: features
        - y: true values
        - scoring: dictionary of metrics
        - cv_rule: cross-validation rule
    """
    scores = cross_validate(model, X, y, scoring=scoring, cv=cv_rule)
    print('Cross-validation error:')
    df_score = pd.DataFrame(scores)
    print(df_score)
    print('\n')
    print(df_score.mean()[2:])


def remove(path):
    if os.path.isfile(path):
        os.remove(path)


if __name__ == '__main__':
    # Get test data
    df = pd.read_csv('./test/test_prepared.csv')
    # Get features and target
    X, y = df.drop('price', axis=1), df['price']

    print('Start cross validation...')
    # Load model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

        # Cross validate it
        cross_validation(X, y, model, scoring=scoring_reg, cv_rule=cv_rule)

    # Remove already useless files
    # remove('./model.pkl') probably we don't need to delete this
    remove('./test/test_prepared.csv')
    remove('./train/train_prepared.csv')
