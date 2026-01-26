'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CheckPrime
//Description:      Check whether number is prime or not
//Input:            Number 
//Output:           Boolean
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def CheckPrime(No):
    count = 0

    for i in range(2,No):
        if No % i == 0:
            count = count + 1
            break

    if count == 1:
        return False
    else:
        return True

def main():
    Value = 0
    bRet = False

    Value = int(input("Enter number : "))

    if Value < 0:
        Value = -Value

    bRet = CheckPrime(Value)

    if bRet == True:
        print("It is prime number")
    else:
        print("It is not prime number")

if __name__ == "__main__":
    main()