import pandas as pd

df = pd.read_csv('Cars.csv')
df_clean = df.dropna(subset=['horsepower'])

year_with_max_avg_mpg = df_clean.groupby('model_year')['mpg'].mean().idxmax()
print("Year with highest average mpg:", year_with_max_avg_mpg)
