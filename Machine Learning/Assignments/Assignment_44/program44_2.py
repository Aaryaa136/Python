import pandas as pd

def Regression(DataPath):

    #------------------------------------------------
    # Step 1 : Load dataset
    #------------------------------------------------
    Border = "-"*40

    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)

    df = pd.read_csv(DataPath)

    print(df.head())

    #------------------------------------------------
    # Step 2 : Explorartory Data Analysis
    #------------------------------------------------
    print(Border)
    print("Step 2 : Explorartory Data Analysis")
    print(Border)

    print("Shape of dataset before removing column : ",df.shape)

    if ('Unnamed: 0') in df.columns:
        df.drop(columns = 'Unnamed: 0' , inplace = True)

    print("Shape of dataset after removing column  : ",df.shape)

    print("Checking missing or null values : ")
    print(df.isnull().sum())

    print("Summary : ")
    print(df.describe())

def main():
    Regression("Advertising.csv")

if __name__ == "__main__":
    main()