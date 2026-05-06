import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv("iris.csv")

    plt.figure(figsize = (8,5))
    sns.boxplot(x = "species" , y = "petal length (cm)" , data = df)

    plt.title("Boxplot : Petal length by variety")
    plt.show()

if __name__ == "__main__":
    main()