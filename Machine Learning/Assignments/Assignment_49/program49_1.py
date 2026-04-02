import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    #-------------------------------------------
    # Step 1 : Load the dataset
    #-------------------------------------------

    print("Step 1 : Loading the dataset")
    df = pd.read_csv("diabetes.csv")
    
    print("Dataset loaded sucessfully")

    print("Few record from dataset : ")
    print(df.head())

    #-------------------------------------------
    # Step 2 : EDA
    #-------------------------------------------

    print("Step 2 : EDA")

    print("Null values if any : ")
    print(df.isnull().sum())

    print(df.describe())

    plt.hist(df["Outcome"])
    plt.title("Distribution of Label")
    plt.show()

    plt.boxplot(df)
    plt.title("Distribution of Label")
    plt.show()


if __name__ == "__main__":
    main()