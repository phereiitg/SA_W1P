import pandas as pd

df = pd.read_csv('Cars.csv')
df_clean = df.dropna(subset=['horsepower'])

count_high_mpg = (df_clean['mpg'] >= 35).sum()
print("Number of cars with mpg ≥ 35:", count_high_mpg)
