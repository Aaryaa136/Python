import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier , plot_tree
from sklearn.metrics import confusion_matrix , accuracy_score , ConfusionMatrixDisplay , classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

print("First five records : ")
print(df.head())

# Step 2 : Analyize the data
print("Shape of dataset : ",df.shape)

print("Attributes : ",list(df.columns))
print(df.describe())

# Step 3 : Visualize the data
sns.histplot(df["StudyHours"])
plt.show()

sns.scatterplot(data = df , x = df["StudyHours"] , y = df["PreviousScore"] , hue = "FinalResult" , palette={0 : "red" , 1 : "green"})
plt.title("Study Hours Vs Previous marks")
plt.xlabel("Study hrs")
plt.ylabel("Previous marks %")
plt.legend()
plt.grid()
plt.show()

# no outliers present
sns.boxplot(df["Attendance"])
plt.title("Attendance Boxplot")
plt.show()

# Step 4 : Split the data for training and testing
features = ["StudyHours" , "Attendance" , "PreviousScore" , "AssignmentsCompleted","SleepHours"]

X = df[features]
Y = df["FinalResult"]

X_train , X_test , y_train , y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 42)
 
model = DecisionTreeClassifier(criterion = "gini" , max_depth = 3 , random_state = 42) 
print("Model used : ",model)

# Step 5 : Train the model
trained_model = model.fit(X_train , y_train)


# Step 6 : Predict / Evaluate the model
y_train_pred = trained_model.predict(X_train)
train_accuracy = accuracy_score(y_train , y_train_pred)

print("Training accuracy is :",train_accuracy * 100 , "%")

y_pred = trained_model.predict(X_test)

# Step 7 : Calculate the accuracy of model
accuracy = accuracy_score(y_test , y_pred)
print("Accuracy is : ",accuracy * 100,"%")

# Step 8 : Confusion matrix generations
cm = confusion_matrix(y_test , y_pred)
print(cm)

cmDisplay = ConfusionMatrixDisplay(confusion_matrix =cm , display_labels = model.classes_)
cmDisplay.plot()

plt.title("Confusion matrix : ")
plt.show()

# Step 9 : Test with new features 
new_features = pd.DataFrame([[6,85,66,7,7]],columns=features)
new_pred = trained_model.predict(new_features)

if(new_pred == 1):
    print("Passed")
elif (new_pred == 0):
    print("Failed")


# Step 10 : Finding Feature score
FeatureScore =  model.feature_importances_
print("Feature scores : ")
for name , score in zip(features,FeatureScore):
    print(f"{name} : {score:.3f}")     # .3f formats score to 3 decimal places

# Only attendance contribute in final result
# Attendance : 1 , rest of features score is 0
