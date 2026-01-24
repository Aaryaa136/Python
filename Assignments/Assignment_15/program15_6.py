'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Minimum
//Description:      Find minimum element from list, using lamda function using reduce
//Input:            List[Numbers]
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             24/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from functools import reduce

def main():
    Size = 0
    Value = 0
    nums = list()

    Size = int(input("Enter number of elements : "))

    if Size < 0:
        Size = -Size

    print("Enter elements : ")
    for i in range(Size):
        Value = int(input())
        nums.append(Value)

    print("Minimum element is : ")
    Minimum = reduce(lambda x , y : x if x < y else y,nums)

    print(Minimum)

if __name__ == "__main__":
    main()