'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CheckEven
//Description:      Check whether number is even, using lamda function
//Input:            Number 
//Output:           Boolean
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

CheckEven = lambda No : No % 2 == 0 

def main():
    Value = None
    bRet = False

    Value = int(input("Enter number : "))


    bRet = CheckEven(Value)

    if bRet == True:
        print(Value,"is even")
    else:
        print(Value,"is odd")   

if __name__ == "__main__":
    main()