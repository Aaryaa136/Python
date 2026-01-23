'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Cube
//Description:      Find cube of number , using lamda function
//Input:            Number
//Output:           Cube
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Cube = lambda No : (No**3)

def main():
    Value = None
    Ret = None

    Value = int(input("Enter number : "))
    if Value < 0:
        Value = -Value

    Ret = Cube(Value)

    print("Cube of",Value,"is :",Ret)

if __name__ == "__main__":
    main()