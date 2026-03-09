import pandas as pd
import math

def EuclideanDist(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans

def main():
    Data = [
            {"Point" : 'A' , "X" : 1 , "Y" : 2 , "Label" : "Red"},
            {"Point" : 'B' , "X" : 2 , "Y" : 3 , "Label" : "Red"},
            {"Point" : 'C' , "X" : 3 , "Y" : 1 , "Label" : "Blue"},
            {"Point" : 'D' , "X" : 6 , "Y" : 5 , "Label" : "Blue"},
            ]

    new_point = {'X' : 2, 'Y' : 2}

    for d in Data:
        d['Distance'] = EuclideanDist(d,new_point)

    for d in Data:
        print(d)

    print()

    sorted_data = sorted(Data , key = lambda values : values['Distance'])

    for d in sorted_data:
        print(d)

    print()

    k = 3
    nearest = sorted_data[:k]

    for d in nearest:
        print(d)

    print()

    Votes = {}

    for neighbour in nearest:
        Label = neighbour["Label"]
        Votes[Label] = Votes.get(Label,0) + 1


    for d in Votes:
        print("Name : ",d ," Number of votes : ",Votes[d])

    predicted_class = max(Votes , key = Votes.get)

    print()

    print("Predicted class is : ",predicted_class)
    

if __name__ == "__main__":
    main()