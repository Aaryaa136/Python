'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Minimum
//Description:      Find minimum for two numbers using lamda function
//Input:            Number , Number
//Output:           Boolean
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Minimum = lambda No1 , No2 : No1 < No2    

def main():
    Value1 = None
    Value2 = None
    bRet = False

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    bRet = Minimum(Value1,Value2)

    if bRet == True:
        print(Value1,"is smaller")
    else:
        print(Value2,"is smaller")   

if __name__ == "__main__":
    main()