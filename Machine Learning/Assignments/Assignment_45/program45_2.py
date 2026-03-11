import pandas as pd

def Classifier(Dataset):
    border = "-"*40

    #-------------------------------------------------------
    # Step 1 : Load the dataset
    #-------------------------------------------------------

    print(border)
    print("Step 1 : Load the dataset")
    print(border)

    df = pd.read_csv(Dataset)

    print("Dataset loaded sucessfully")

    print(df.head())

    #-------------------------------------------------------
    # Step 2 : Explorartoy Data Analysis
    #-------------------------------------------------------

    print(border)
    print("Step 2 : Explorartoy Data Analysis")
    print(border)

    print("Shape is : ",df.shape)

    print("Null rows : ")
    print(df.isnull().sum())

    print(df.describe())

def main():
    Classifier("WinePredictor.csv")

if __name__ == "__main__":
    main()