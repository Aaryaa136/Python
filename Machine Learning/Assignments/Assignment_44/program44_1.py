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

def main():
    Regression("Advertising.csv")

if __name__ == "__main__":
    main()