'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Addition
//Description:      Accept two number and add , using lamda
//Input:            Number , Number
//Output:           Add
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Addition = lambda No1 , No2 : No1 + No2  

def main():
    Value1 = None
    Value2 = None
    Ret = 0

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Addition(Value1,Value2)

    print("Addition is : ",Ret)   

if __name__ == "__main__":
    main()