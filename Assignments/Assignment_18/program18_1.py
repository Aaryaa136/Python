'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    AddList
//Description:      Addition of elements in list
//Input:            Size , List
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def AddList(length,Arr):
    sum = 0

    for i in range(length):
        sum = sum + Arr[i]
    
    return sum

def main():
    size = 0
    value = 0
    Ret = 0

    nums = list()

    size = int(input("Enter number of elements : "))

    if size < 0:
        size = -size

    print("Enter elements : ")
    
    for i in range(size):
        value = int(input())
        nums.append(value)

    print("Elements in list :")
    print(nums)

    Ret = AddList(size,nums)

    print("Addition of elements is :",Ret)

if __name__ == "__main__":
    main()