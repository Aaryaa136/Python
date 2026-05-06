import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv("iris.csv")
    
    sns.countplot(x = "species" , data = df)
    plt.title("Count of each Variety")

    plt.show()

if __name__ == "__main__":
    main()