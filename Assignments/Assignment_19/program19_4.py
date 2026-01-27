from functools import reduce

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Even ,Sqaure , Summation 
//Description:      Use filter , map and reduce for above mentioned functions
//Input:            List , List , List
//Output:           List , List , Number
//Author:           Aaryaa Nandkumar Patil
//Date:             26/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Even(No):
    return No % 2 == 0

def Square(No):
    return No ** 2

def Summation(a,b):
    return a + b

def main():
    Length = 0
    Value = 0
    nums = []
    
    Length = int(input("Enter number of elements : "))
    if Length < 0:
        Length = -Length

    print("Enter elements : ")

    for i in range(Length):
        Value = int(input())
        nums.append(Value)

    print(nums)

    FData = list(filter(Even,nums))
    print("Data after filter :",FData)

    MData = list(map(Square,FData))
    print("Data after map :",MData)

    RData = reduce(Summation,MData)
    print("Sum is :",RData)

if __name__ == "__main__":
    main()