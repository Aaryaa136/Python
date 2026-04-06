import pandas as pd
import numpy as np 

from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.compose import ColumnTransformer

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score , confusion_matrix , classification_report 

def main():
    Border = "-"*40

    #------------------------------------------
    # Step 1 : Load the dataset
    #------------------------------------------

    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)

    df = pd.read_csv("bank-full.csv", sep=';')

    print("Dataset loaded successfully")

    print("Few records from dataset : ")
    print(df.head(10))

    #------------------------------------------
    # Step 2 : EDA
    #------------------------------------------

    print(Border)
    print("Step 2 : EDA")
    print(Border)

    print("Shape of dataset : ")
    print(df.shape)

    print("Missing values : ")
    print(df.isnull().sum())

    print(df.describe())

    for col in df.columns:
        print(col, (df[col] == "unknown").sum())

    # Replace 'unknown' with NaN
    df.replace("unknown", np.nan, inplace=True)

    # Fill missing values 
    df['job'] = df['job'].fillna(df['job'].mode()[0])
    df['education'] = df['education'].fillna(df['education'].mode()[0])

    df['contact'] = df['contact'].fillna("missing")
    df['poutcome'] = df['poutcome'].fillna("not_contacted")

    # Check again after cleaning
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    #------------------------------------------
    # Step 3 : Data preprocessing
    #------------------------------------------

    print(Border)
    print("Step 3 : Data preprocessing")
    print(Border)

    X = df.drop('y', axis=1)
    Y = df['y']

    encoder = X.select_dtypes(include=['object']).columns
    scaling = X.select_dtypes(exclude=['object']).columns

    print("Categorical columns :",list(encoder))
    print("Numerical columns :",list(scaling))

    # create transformer
    preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), scaling),
        ('cat', OneHotEncoder(drop='first',sparse_output=False), encoder)
    ]
    )
    
    # fit and tranform the features
    X_scaled = preprocessor.fit_transform(X)

    print("Processed features shape :",X_scaled.shape)

    #------------------------------------------
    # Step 4 : Splitting the data 
    #------------------------------------------

    print(Border)
    print("Step 4 : Splitting the data ")
    print(Border)

    X_train , X_test , Y_train , Y_test = train_test_split(X_scaled,Y,test_size=0.2,random_state=42)

    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    #------------------------------------------
    # Step 5 : Train the model
    #------------------------------------------

    print(Border)
    print("Step 5 : Train the model")
    print(Border)

    lr_model = LogisticRegression()
    lr_model.fit(X_train,Y_train)

    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train,Y_train)

    rf_model = RandomForestClassifier()
    rf_model.fit(X_train,Y_train)

    print("Models used :",lr_model,knn_model,rf_model)

    #------------------------------------------
    # Step 6 : Evaluate the model
    #------------------------------------------

    print(Border)
    print("Step 6 : Evaluate the model")
    print(Border)

    lr_pred = lr_model.predict(X_test)
    knn_pred = knn_model.predict(X_test)
    rf_pred = rf_model.predict(X_test)

    print("Accuracy of Logistic regression :",accuracy_score(Y_test,lr_pred)*100)
    print("Accuracy of KNN  :",accuracy_score(Y_test,knn_pred)*100)
    print("Accuracy of Random Forest :",accuracy_score(Y_test,rf_pred)*100)

    #------------------------------------------------------------------------

    print("Confusion matrix for Logistic Regression : ")
    print(confusion_matrix(Y_test,lr_pred))

    print("Confusion matrix for KNN : ")
    print(confusion_matrix(Y_test,knn_pred))

    print("Confusion matrix for Random Forest : ")
    print(confusion_matrix(Y_test,rf_pred))    

    #------------------------------------------------------------------------

    print("Classification report for Logistic Regression : ")
    print(classification_report(Y_test,lr_pred))

    print("Classification report for KNN : ")
    print(classification_report(Y_test,knn_pred))

    print("Classification report for Random Forest: ")
    print(classification_report(Y_test,rf_pred))

if __name__ == "__main__":
    main()