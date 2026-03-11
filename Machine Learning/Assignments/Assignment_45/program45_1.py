import pandas as pd

def Classifier(Dataset):

    #-------------------------------------------------------
    # Step 1 : Load the dataset
    #-------------------------------------------------------

    border = "-"*40
    print(border)
    print("Step 1 : Load the dataset")
    print(border)

    df = pd.read_csv(Dataset)

    print("Dataset loaded sucessfully")

def main():
    Classifier("WinePredictor.csv")

if __name__ == "__main__":
    main()