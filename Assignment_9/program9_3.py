'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Square
//Description:      To find square of given number
//Input:            Number
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             17/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Sqaure(No):
    Ans = None
    Ans = No * No
    return Ans

def main():
    Value = None
    Result = None

    print("Enter number : ")
    Value = int(input())

    Result = Sqaure(Value)

    print("Square of",Value,"is :",Result)

if __name__ == "__main__":
    main()