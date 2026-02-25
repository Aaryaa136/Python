import pandas as pd

# Load the dataset
Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

print("First five records : ")
print(df.head())

print("Last five records : ")
print(df.tail())

print("Shape of dataset : ",df.shape)

print("Attributes : ",list(df.columns))

print("Type of attributes : ")
print(df.dtypes)

print("Total number of students : ",len(df))   # df.shape[0]
print("Total number of students passed : ",(df["FinalResult"] == 1).sum())
print("Total number of failed student : ",(df["FinalResult"] == 0).sum())

print("Average study hours : ",(df["StudyHours"]).mean())
print("Average attendence of students : ",(df["Attendance"]).mean())
print("Maximum previous score is : ",(df["PreviousScore"]).max())
print("Minimum sleep hour is : ",(df["SleepHours"]).min())