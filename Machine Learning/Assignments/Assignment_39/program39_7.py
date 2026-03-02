import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier , plot_tree
from sklearn.metrics import confusion_matrix , accuracy_score , ConfusionMatrixDisplay , classification_report
import matplotlib.pyplot as plt

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

print("First five records : ")
print(df.head())

print("Shape of dataset : ",df.shape)

print("Attributes : ",list(df.columns))

features = ["StudyHours" , "Attendance" , "PreviousScore" , "AssignmentsCompleted","SleepHours"]

X = df[features]
Y = df["FinalResult"]

X_train , X_test , y_train , y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 42)
 
model = DecisionTreeClassifier(criterion = "gini" , max_depth = 3 , random_state = 42) 
print("Model used : ",model)

trained_model = model.fit(X_train , y_train)

y_train_pred = trained_model.predict(X_train)
train_accuracy = accuracy_score(y_train , y_train_pred)

print("Training accuracy is :",train_accuracy * 100 , "%")

y_pred = trained_model.predict(X_test)

cm = confusion_matrix(y_test , y_pred)
print(cm)

accuracy = accuracy_score(y_test , y_pred)
print("Accuracy is : ",accuracy * 100,"%")

cmDisplay = ConfusionMatrixDisplay(confusion_matrix =cm , display_labels = model.classes_)
cmDisplay.plot()

plt.title("Confusion matrix : ")
plt.show()

new_features = [[6,85,66,7,7]]
new_pred = trained_model.predict(new_features)

if(new_pred == 1):
    print("Passed")
elif (new_pred == 0):
    print("Failed")
