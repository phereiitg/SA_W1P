import pandas as pd

df = pd.read_csv('Cars.csv')
df_clean = df.dropna(subset=['horsepower'])

mean_accel_japan = round(df_clean[df_clean['origin'] == 'japan']['acceleration'].mean(), 2)
print("Mean acceleration (Japan):", mean_accel_japan)
