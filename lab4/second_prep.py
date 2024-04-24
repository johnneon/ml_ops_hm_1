import pandas as pd
from sklearn.preprocessing import PowerTransformer

# Read dataset
df = pd.read_csv('./datasets/data.csv')

# Prep power transformer
power = PowerTransformer(method='yeo-johnson')
power.fit(df)

# Transform data
power_df = power.transform(df)

# Save new version of dataset
power_df.to_csv('./datasets/data.scv')
