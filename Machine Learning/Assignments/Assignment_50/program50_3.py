import pandas as pd
import numpy as np 

from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.compose import ColumnTransformer

from sklearn.model_selection import train_test_split

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

if __name__ == "__main__":
    main()