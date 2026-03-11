import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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

    #-------------------------------------------------------
    # Step 3 : Split dataset into training and testing
    #-------------------------------------------------------

    X = df.drop('Class' , axis=1)
    Y = df['Class']

    print(border)
    print("Step 3 : Split dataset into training and testing")
    print(border)

    print("Features shape : ")
    print(X.columns)

    X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size=0.2 , random_state=42)

    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    #-------------------------------------------------------
    # Step 4 : Train the model
    #-------------------------------------------------------

    print(border)
    print("Step 4 : Train the model")
    print(border)

    model = DecisionTreeClassifier(max_depth=3)

    model.fit(X_train,Y_train)

    print("Model trained usig : ",model)

    #-------------------------------------------------------
    # Step 5 : Test the model
    #-------------------------------------------------------

    print(border)
    print("Step 5 : Test the model")
    print(border)

    Y_pred = model.predict(X_test)

    print("Model tested")

def main():
    Classifier("WinePredictor.csv")

if __name__ == "__main__":
    main()