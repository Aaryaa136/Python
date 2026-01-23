'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Square
//Description:      Find square of number , using lamda function
//Input:            Number
//Output:           Square
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Square = lambda No : (No**2)

def main():
    Value = None
    Ret = None

    Value = int(input("Enter number : "))

    Ret = Square(Value)

    print("Square of",Value,"is :",Ret)

if __name__ == "__main__":
    main()