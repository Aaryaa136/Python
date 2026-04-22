import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score

def MarvellousAdvertise(DataPath):
    Border = "-"*40

    #-----------------------------------------------------------
    #   Step 1 : Load Dataset
    #-----------------------------------------------------------
    print(Border)
    print("Step : Load Dataset")
    print(Border)
    df = pd.read_csv(DataPath)

    print("Few records from the dataset : ")
    print(df.head())

    #-----------------------------------------------------------
    #   Step 2 : Remove unwanted columns
    #-----------------------------------------------------------

    print(Border)
    print("Step 2 : Remove unwanted columns")
    print(Border)

    print("Shape of dataset before removal : ",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns = 'Unnamed: 0' , inplace = True)

    print("Shape of dataset after removal : ",df.shape)

    print(Border)
    print("Clean dataset is : ")
    print(Border)

    print(df.head())

    #-----------------------------------------------------------
    #   Step 3 : Check missing values
    #-----------------------------------------------------------

    print(Border)
    print("Step 3 : Check missing values")
    print(Border)

    print("Missing values count : ")
    print(df.isnull().sum())

    #-----------------------------------------------------------
    #   Step 4 : Display statistical summary
    #-----------------------------------------------------------

    print(Border)
    print("Step 4 : Display statistical summary")
    print(Border)

    print(df.describe())

    #-----------------------------------------------------------
    #   Step 5 : Correlation between columns
    #-----------------------------------------------------------

    print(Border)
    print("Step 5 : Correlation between columns")
    print(Border)

    print("Correlation matrix : ")
    print(df.corr())

def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()