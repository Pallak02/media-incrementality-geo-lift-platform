import pandas as pd

# Read dataset
df = pd.read_csv("Data/dt_simulated_weekly.csv")

print("=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print(df.shape)

print("\n")

print("=" * 50)
print("COLUMNS")
print("=" * 50)
print(df.columns.tolist())

print("\n")

print("=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(df.head())

print("\n")

print("=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())