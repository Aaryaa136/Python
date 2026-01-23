'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CheckDivisibleFive
//Description:      Check whether number is divisible by 5 or not using, lamda function
//Input:            Number 
//Output:           Boolean
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

CheckDivisibleFive = lambda No : No % 5 == 0 

def main():
    Value = None
    bRet = False

    Value = int(input("Enter number : "))

    bRet = CheckDivisibleFive(Value)

    if bRet == True:
        print(Value,"is divisible by 5")
    else:
        print(Value,"is not divisible by 5")   

if __name__ == "__main__":
    main()