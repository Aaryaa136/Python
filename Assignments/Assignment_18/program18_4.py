'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Frquency
//Description:      Count frquency of number given by user from list
//Input:            Size , List , Number
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Frequency(length,Arr,val):
    count = 0

    for i in range(length):
        if Arr[i] == val:
            count = count + 1
        
    return count

def main():
    size = 0
    value = 0
    Ret = 0
    number = 0

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

    number = int(input("Enter a number : "))
    
    Ret = Frequency(size,nums,number)

    print("Frequency of:",number,"is :",Ret)

if __name__ == "__main__":
    main()