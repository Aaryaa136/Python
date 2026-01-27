'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    MMultiplication
//Description:      Multiplication of two numbers using lambda function
//Input:            Number , Number
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             26/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


Multiplication = lambda No1 , No2 : No1 * No2

def main():
    Value1 = 0
    Ret = 0

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter first number : "))  

    Ret = Multiplication(Value1,Value2)

    print("Multiplication is :",Ret)

if __name__ == "__main__":
    main()