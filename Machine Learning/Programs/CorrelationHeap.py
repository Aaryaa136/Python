import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv("iris.csv")
    
    corr = df.select_dtypes(include=["float64" , "int64"]).corr()

    plt.figure(figsize = (7,5))
    sns.heatmap(corr , annot = True , cmap = "coolwarm")
    plt.title("Correlation Matrix")

    plt.show()

if __name__ == "__main__":
    main()