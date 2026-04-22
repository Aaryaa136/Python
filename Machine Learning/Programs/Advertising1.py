import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def main():
    df = pd.read_csv("Advertising.csv")

    print(df.shape)

    # Data cleaning
    if 'Unammed: 0' in df.columns:
        df.drop(columns = ['Unamed: 0'] , inplace = True)

    print(df.shape)

if __name__ == "__main__":
    main()