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

passed = (df["FinalResult"] == 1).sum()
failed = (df["FinalResult"] == 0).sum()
print("Total number of students passed : ",passed)
print("Total number of failed student : ",failed)

print("Average study hours : ",(df["StudyHours"]).mean())
print("Average attendence of students : ",(df["Attendance"]).mean())
print("Maximum previous score is : ",(df["PreviousScore"]).max())
print("Minimum sleep hour is : ",(df["SleepHours"]).min())

print("Distribution of label : ")

pass_percentage = (passed / len(df)) * 100
failed_percentage = (failed / len(df)) * 100

print(df["FinalResult"].value_counts())
print("Pass percentage : ",pass_percentage,"%")
print("Failed percentage : ",failed_percentage,"%")

'''
Study Hours plays a crucial factor :  high number of study hours 
                                      makes higher chance of passing
Study hours below 4.5 hours : less chance of passing

Yes , higher attendance improves Final Result
According to my observation attendance more than 75%  increases chances of passing exam                                    

'''