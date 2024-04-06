import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder


def preparation_data(path):
    df = pd.read_csv(path)

    df.drop(['ID'], axis=1, inplace=True)

    cat_columns = []
    num_columns = []

    for column_name in df.columns:
        if df[column_name].dtypes == object:
            cat_columns += [column_name]
        else:
            num_columns += [column_name]

    scaler = StandardScaler()
    scaler.fit(df[num_columns])
    df[num_columns] = scaler.transform(df[num_columns])

    encoder = OrdinalEncoder()
    encoder.fit(df[cat_columns])
    df[cat_columns] = encoder.transform(df[cat_columns])

    return df


if __name__ == '__main__':
    train = preparation_data('./train/train.csv')
    train.to_csv('./train/train_prepared.csv')

    test = preparation_data('./test/test.csv')
    test.to_csv('./test/test_prepared.csv')
