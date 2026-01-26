'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    SumDigits
//Description:      Sum digits in given number
//Input:            Number 
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def SumDigits(No):
    sum = 0
    Digit = 0

    while No != 0:
        Digit = No % 10
        sum = sum + Digit
        No = No // 10

    return sum

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = SumDigits(Value)

    print("Sum of digits in",Value,"is :",Ret)

if __name__ == "__main__":
    main()