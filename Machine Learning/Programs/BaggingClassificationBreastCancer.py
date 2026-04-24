import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier              # homogenous ensemble
from sklearn.metrics import accuracy_score , classification_report , confusion_matrix

#------------------------------------------------------------------
# Step 1 : Load the dataset
#------------------------------------------------------------------

df = pd.read_csv("breast_cancer.csv")
print("Shape of dataset :",df.shape)
print("First 5 records :")
print(df.head())

#------------------------------------------------------------------
# Step 2 : Seperate feature and labels 
#------------------------------------------------------------------

X = df.drop("target",axis=1)
Y = df["target"]

#------------------------------------------------------------------
# Step 3 : Split dataset for training and testing 
#-------------------------------------------------------------------

X_train , X_test , Y_train , Y_test = train_test_split(X , Y , train_size=0.2 , random_state=42)

#------------------------------------------------------------------
# Step 4 : Create base model
#-------------------------------------------------------------------

base_model = DecisionTreeClassifier(random_state=42)

#------------------------------------------------------------------
# Step 5 : Create bagging model
#-------------------------------------------------------------------

bagging_model = BaggingClassifier(
                                   estimator=base_model,
                                   n_estimators=10,
                                   random_state=42
                                )

#------------------------------------------------------------------
# Step 6 : Train bagging model
#-------------------------------------------------------------------

bagging_model.fit(X_train,Y_train)  

#------------------------------------------------------------------
# Step 7 : Test bagging model
#-------------------------------------------------------------------

Y_pred = bagging_model.predict(X_test)

#------------------------------------------------------------------
# Step 8 : Evaluate the model
#-------------------------------------------------------------------

print("Bagging Accuracy :",accuracy_score(Y_test,Y_pred)*100)

print("Confusion matrix :")
print(confusion_matrix(Y_test,Y_pred))