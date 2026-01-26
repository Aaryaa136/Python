'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Maximum
//Description:      Find maximum element from list
//Input:            Size , List
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def Maximum(length,Arr):
    max = 0
    max = Arr[0]

    for i in range(length):
        if Arr[i] > max:
            max = Arr[i]
        
    return max

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

    Ret = Maximum(size,nums)

    print("Maximum element is :",Ret)

if __name__ == "__main__":
    main()