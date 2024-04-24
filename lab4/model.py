import pandas as pd
from sklearn.datasets import load_iris

# Download dataset
dataset = load_iris()

# Make it df
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target

# Save dataset
df.to_csv('./datasets/data.csv', index=False)
