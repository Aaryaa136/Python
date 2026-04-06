import pandas as pd
import numpy as np 

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
    print(df.head())

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


if __name__ == "__main__":
    main()