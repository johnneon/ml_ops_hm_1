import pickle

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Download dataset
dataset = load_iris()

# Make it df
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target
df.to_csv('./data.csv', index=False)

X, y = df.drop(columns='target'), df['target']

# Some data preparation
scaler = StandardScaler()
scaler.fit(X)

# Split it out
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

# Save model and preps
with open('./model.pkl', 'wb') as file:
    pickle.dump((model, scaler), file)
