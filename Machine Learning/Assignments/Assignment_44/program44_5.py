import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score

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

    #------------------------------------------------
    # Step 2 : Explorartory Data Analysis
    #------------------------------------------------
    print(Border)
    print("Step 2 : Explorartory Data Analysis")
    print(Border)

    print("Shape of dataset before removing column : ",df.shape)

    if ('Unnamed: 0') in df.columns:
        df.drop(columns = 'Unnamed: 0' , inplace = True)

    print("Shape of dataset after removing column  : ",df.shape)

    print("Checking missing or null values : ")
    print(df.isnull().sum())

    print("Summary : ")
    print(df.describe())

    #------------------------------------------------
    # Step 3 : Independent and dependent variables
    #------------------------------------------------
    print(Border)
    print("Step 3 : Independent and dependent variables")
    print(Border)

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of independent variables : ",X.shape)
    print("Shape of dependent variables : ",Y.shape)

    #------------------------------------------------
    # Step 4 : Split data for training and testing
    #------------------------------------------------
    print(Border)
    print("Step 4 : Split data for training and testing")
    print(Border)

    X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 42)

    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape )

    #------------------------------------------------
    # Step 5 : Create and train the model
    #------------------------------------------------
    print(Border)
    print("Step 5 : Create and train the model")
    print(Border)

    model = LinearRegression()

    print("Model used : ",model)
    
    model.fit(X_train , Y_train)

    #------------------------------------------------
    # Step 6 : Test the model
    #------------------------------------------------
    print(Border)
    print("Step 6 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)

    #------------------------------------------------
    # Step 7 : Evaluate the model
    #------------------------------------------------
    print(Border)
    print("Step 7 : Evaluate the model")
    print(Border)

    RME = mean_squared_error(Y_test , Y_pred)
    r2 = r2_score(Y_test , Y_pred)

    print("Root mean Square error : ",RME)
    print("R2 score : ",r2)

    #------------------------------------------------
    # Step 8 : Actual Vs Expected values
    #------------------------------------------------
    print(Border)
    print("Step 7 : Actual Vs Expected")
    print(Border)

    Result = pd.DataFrame({
            'Actual' : Y_test.values,
            'Predicted' : Y_pred   
            })

    print(Result.head(10))

    print(Border)
    
def main():
    Regression("Advertising.csv")

if __name__ == "__main__":
    main()