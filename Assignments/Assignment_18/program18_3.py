'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Minimum
//Description:      Find minimum element from list
//Input:            Size , List
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Minimum(length,Arr):
    min = 0
    min = Arr[0]

    for i in range(length):
        if Arr[i] < min:
            min = Arr[i]
        
    return min

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

    Ret = Minimum(size,nums)

    print("Minimum element is :",Ret)

if __name__ == "__main__":
    main()