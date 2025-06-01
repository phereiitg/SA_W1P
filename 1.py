import pandas as pd

df = pd.read_csv('Cars.csv')
df_clean = df.dropna(subset=['horsepower'])
car_with_max_hp = df_clean.loc[df_clean['horsepower'].idxmax(), 'name']
print("Car with highest horsepower:", car_with_max_hp)
