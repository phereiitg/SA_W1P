import pandas as pd

df = pd.read_csv('Cars.csv')
df_clean = df.dropna(subset=['horsepower'])

filtered_cars = df_clean[(df_clean['horsepower'] > 100) & (df_clean['weight'] < 3000)]
most_common_origin = filtered_cars['origin'].mode()[0]

print("Most common origin:", most_common_origin)
