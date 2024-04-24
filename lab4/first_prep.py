import pandas as pd
from sklearn.preprocessing import StandardScaler

# Read dataset
df = pd.read_csv('./datasets/data.csv')

# Prep scaler
scaler = StandardScaler()
scaler.fit(df)

# Transform data
scaled_df = scaler.transform(df)

# Save new version of dataset
pd.DataFrame(scaled_df, columns=df.columns).to_csv('./datasets/data.csv')
