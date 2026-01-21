'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CountDigits
//Description:      Count number of digits in a number
//Input:            Number
//Output:           Count
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def CountDigits(No):
    Digit = 0
    iCount = 0

    if No < 0:
        No = -No 

    while (No != 0):
        Digit = No % 10
        iCount = iCount + 1
        No = No // 10

    return iCount

def main():
    Value = None
    Result = None

    Value = int(input("Enter number : "))

    Result = CountDigits(Value)
    print("Digits in",Value,"are :",Result)

if __name__ == "__main__":
    main()