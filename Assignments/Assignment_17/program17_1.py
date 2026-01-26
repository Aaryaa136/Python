import Arithmetic

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    main
//Description:      Create a module arithmetic : add , sub , multi and div and import it
//Input:            Number , Number
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Arithmetic.Add(Value1,Value2)
    print("Addition is :",Ret)

    Ret = Arithmetic.Sub(Value1,Value2)
    print("Substraction is :",Ret)

    Ret = Arithmetic.Multi(Value1,Value2)
    print("Multiplication is :",Ret)

    Ret = Arithmetic.Div(Value1,Value2)
    print("Division is :",Ret)

if __name__ == "__main__":
    main()
