'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Range ,Increment , Product 
//Description:      Use filter , map and reduce for above mentioned functions
//Input:            List , List , List
//Output:           List , List , Number
//Author:           Aaryaa Nandkumar Patil
//Date:             26/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from functools import reduce

def Range(No):
    return No >= 70 and No <= 90
    
def Increment(No):
    return No + 10

def Product(a,b):
    return  a * b
    
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

    FData = list(filter(Range,nums))
    print("Data after filter :",FData)

    MData = list(map(Increment,FData))
    print("Data after map :",MData)

    RData = reduce(Product,MData)
    print("Sum is :",RData)

if __name__ == "__main__":
    main()