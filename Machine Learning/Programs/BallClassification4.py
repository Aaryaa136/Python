from sklearn import tree

# Rough = 1
# Smooth = 0

# Cricket = 2
# Tennis = 1

def main():
    print("Ball Classification case study")

    # Independent Variables
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    # Dependent Variables
    Y = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    modelobj = tree.DecisionTreeClassifier()           # modelobj is a object of DTC

    trainedmodel = modelobj.fit(X,Y)

    Result = trainedmodel.predict([[37,1],[94,0]])          #  1     2

    print("Model predicts the object as :",Result)

if __name__ == "__main__":
    main()                               