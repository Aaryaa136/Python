import pandas as pd
import numpy as np 

from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.compose import ColumnTransformer

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

if __name__ == "__main__":
    main()