import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

import pickle

separator = '===================================='

# Get data from prepared csv
df = pd.read_csv('./train/train_prepared.csv')

# Get features and target
X, y = df.drop('price', axis=1), df['price']

# Split it out
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Crate model
lr = LinearRegression()

print('Start learning model...')

# Fit
lr.fit(X_train, y_train)

print('Finished learning')

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(lr, f)

print('Model has been saved')
print(separator)
print(separator)

