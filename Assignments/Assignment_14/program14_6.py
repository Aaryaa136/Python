'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CheckOdd
//Description:      Check whether number is odd using lamda function
//Input:            Number 
//Output:           Boolean
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

CheckOdd = lambda No : No % 2 != 0 

def main():
    Value = None
    bRet = False

    Value = int(input("Enter number : "))

    bRet = CheckOdd(Value)

    if bRet == True:
        print(Value,"is odd")
    else:
        print(Value,"is even")   

if __name__ == "__main__":
    main()