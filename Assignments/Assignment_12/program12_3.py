'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Arithmetic
//Description:      Performs arithmetic operations : addition,substraction,multiplication,division
//Input:            Number , Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             18/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Arithmetic(No1, No2):
    def Add():
        return No1 + No2

    def Sub():
        return No1 - No2

    def Multi():
        return No1 * No2

    def Div():
        return No1 / No2

    print("Addition :", Add())
    print("Subtraction :", Sub())
    print("Multiplication :", Multi())
    print("Division :", Div())


def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Arithmetic(Value1, Value2)

if __name__ == "__main__":
    main()
