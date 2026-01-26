from MarvellousNum import CheckPrime 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    AddPrime
//Description:      Create a module , to check prime , import it and return sum of prime number from list
//Input:            List
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def AddPrime(nums):
    return sum(filter(CheckPrime,nums))

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
    
    Ret = AddPrime(nums)

    print("Sum of prime numbers :",Ret)

if __name__ == "__main__":
    main()