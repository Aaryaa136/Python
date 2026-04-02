import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score , confusion_matrix , classification_report

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
    plt.title("Feature distribution")
    plt.show()

    sns.boxplot(data = df)
    plt.title("Feature distribution")
    plt.show()

    #-------------------------------------------
    # Step 3 : Preprocessing data
    #-------------------------------------------

    print("Step 3 : Preprocessing data")

    cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

    for col in cols:
        df[col] = df[col].replace(0, df[col].median())


    X = df.drop("Outcome",axis=1)
    Y = df["Outcome"]

    print("Indepedent variables : ")
    print(X.columns)

    print("Dependent variable : ")
    print(Y.name)

    #-------------------------------------------
    # Step 4 : Spliting and scaling
    #-------------------------------------------

    print("Step 4 : Spliting and scaling")

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    scaler = StandardScaler()
     
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Shapes : ")
    print("X_train shape :",X_train.shape)
    print("X_test shape :",X_test.shape)
    print("Y_train shape :",Y_train.shape)
    print("Y_test shape :",Y_test.shape)

    #-------------------------------------------
    # Step 5 : Model selection
    #-------------------------------------------

    print("Step 5 : Model selection")

    lr_model = LogisticRegression()
    print("Model used :",lr_model)
    
    knn_model = KNeighborsClassifier(n_neighbors=5)
    print("Model used : ",knn_model)

    #-------------------------------------------
    # Step 6 : Train the model
    #-------------------------------------------

    print("Step 6 : Train the model")

    lr_model.fit(X_train,Y_train)
    knn_model.fit(X_train,Y_train)

    print("Model trained sucessfully")

    #-------------------------------------------
    # Step 7 : Test the model
    #-------------------------------------------

    print("Step 7 : Test the model")
    lr_pred = lr_model.predict(X_test)
    knn_pred = knn_model.predict(X_test)

    #-------------------------------------------
    # Step 8 : Evaluate  the model
    #-------------------------------------------

    print("Step 8 : Evaluate the model")

    lr_accuracy = accuracy_score(Y_test,lr_pred)
    knn_accuracy = accuracy_score(Y_test,knn_pred)

    print("Logistic regression accuracy is :")
    print(lr_accuracy*100)

    print("KNN accuracy is :")
    print(knn_accuracy*100)

    print("Confusion matrix of Logistic Regression :")
    print(confusion_matrix(Y_test,lr_pred))

    print("Confusion matrix of KNN Classifier :")
    print(confusion_matrix(Y_test,knn_pred))

    print("Classification Report (Logistic Regression) :")
    print(classification_report(Y_test,lr_pred))

    print("Classification Report (KNN) :")
    print(classification_report(Y_test,knn_pred))

    cm_lr = confusion_matrix(Y_test, lr_pred)

    plt.figure(figsize=(5,4))
    sns.heatmap(
    cm_lr,
    annot=True,            # show numbers
    fmt='d',               # integer format
    cmap='Blues',
    xticklabels=["No Diabetes", "Diabetes"],
    yticklabels=["No Diabetes", "Diabetes"]
    )

    plt.title("Confusion matrix : Logistic Regression")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()


if __name__ == "__main__":
    main()