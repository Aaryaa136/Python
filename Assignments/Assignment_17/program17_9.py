'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CountDigits
//Description:      Count digits in given number
//Input:            Number 
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def CheckDigits(No):
    count = 0
    Digit = 0

    while No != 0:
        Digit = No % 10
        count = count + 1
        No = No // 10

    return count

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = CheckDigits(Value)

    print("Number of digits in",Value,"are :",Ret)

if __name__ == "__main__":
    main()