'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Maximum
//Description:      Find maximum for two numbers using lamda function
//Input:            Number , Number
//Output:           Boolean
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Maximum = lambda No1 , No2 : No1 > No2    #return T/F

def main():
    Value1 = None
    Value2 = None
    bRet = False

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    bRet = Maximum(Value1,Value2)

    if bRet == True:
        print(Value1,"is greater")
    else:
        print(Value2,"is greater")   

if __name__ == "__main__":
    main()