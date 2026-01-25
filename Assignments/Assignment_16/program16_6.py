'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    NumberType
//Description:      Check type of number : +ve , -ve or 0
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             24/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def NumberType(No):
    if No < 0:
        print("Negative number")
    elif No > 0:
        print("Positive number")
    else:
        print("Zero")

def main():
    Value = 0

    Value = int(input("Enter number : "))
        
    NumberType(Value)

if __name__ == "__main__":
    main()