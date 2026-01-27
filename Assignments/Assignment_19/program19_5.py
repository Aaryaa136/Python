from functools import reduce

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Prime , MultiplyTwo , Maximum
//Description:      Use filter , map and reduce for above mentioned functions
//Input:            List , List , List
//Output:           List , List , Number
//Author:           Aaryaa Nandkumar Patil
//Date:             26/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Prime(No):
    for i in range(2,No):
        if No % i == 0:
            return None
    return No

def MultiplyTwo(No):
    return No * 2

def Maximum(a,b):
    if a > b:
        return a
    else:
        return b

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

    FData = list(filter(Prime,nums))
    print("Data after filter :",FData)

    MData = list(map(MultiplyTwo,FData))
    print("Data after map :",MData)

    RData = reduce(Maximum,MData)
    print("Maximum element is :",RData)

if __name__ == "__main__":
    main()