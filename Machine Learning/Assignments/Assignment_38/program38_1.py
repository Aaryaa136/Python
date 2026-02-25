import pandas as pd

# Load the dataset
Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

print("First five records : ")
print(df.head())
print()

print("Last five records : ")
print(df.tail())
print()

print("Shape of dataset : ",df.shape)
print()

print("Attributes : ",list(df.columns))
print()

print("Type of attributes : ")
print(df.dtypes)
