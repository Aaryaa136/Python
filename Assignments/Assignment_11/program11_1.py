'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CheckPrime
//Description:      Check whether number is prime
//Input:            Number
//Output:           Boolean
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def CheckPrime(No):
    bFlag = False

    for i in range(0,int(No/2)):
        if (No % i == 0):
            bFlag = False

    return bFlag
        
def main():
    Value = 0
    bRet = False

    Value = int(input("Enter number : "))

    bRet = CheckPrime(Value)

    if bRet == True:
        print(Value,"is Prime number")
    else:
        print(Value,"is not Prime number")

if __name__ == "__main__":
    main()