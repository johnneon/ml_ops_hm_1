import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder


def preparation_data(path):
    """
    Prepare the data for ML

    Params:
        - path (str): path to file with data

    Returns:
        - data (pd.DataFrame): dataframe with prepared data
    """

    # Get dataset from file
    df = pd.read_csv(path)

    # Remove useless column
    df.drop(['ID'], axis=1, inplace=True)

    # Divide features for cat/num
    cat_columns = []
    num_columns = []

    for column_name in df.columns:
        if df[column_name].dtypes == object:
            cat_columns += [column_name]
        else:
            num_columns += [column_name]

    # Scaling num features
    scaler = StandardScaler()
    scaler.fit(df[num_columns])
    df[num_columns] = scaler.transform(df[num_columns])

    # Encode cat features
    encoder = OrdinalEncoder()
    encoder.fit(df[cat_columns])
    df[cat_columns] = encoder.transform(df[cat_columns])

    return df


if __name__ == '__main__':
    # Prep train data
    train = preparation_data('./train/train.csv')
    # Save it
    train.to_csv('./train/train_prepared.csv')

    # Prep train data
    test = preparation_data('./test/test.csv')
    # Save it
    test.to_csv('./test/test_prepared.csv')
