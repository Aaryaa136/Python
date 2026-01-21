'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    SumDigits
//Description:      Sum of digits of a number
//Input:            Number
//Output:           Summation
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def SumDigits(No):
    Digit = 0
    Sum = 0

    if No < 0:
        No = -No 

    while (No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10
    
    return Sum

def main():
    Value = None
    Result = 0

    Value = int(input("Enter number : "))

    Result = SumDigits(Value)
    print("Sum of ",Value,"is:",Result)

if __name__ == "__main__":
    main()