'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Cube
//Description:      To find cube of given number
//Input:            Number
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             17/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Cube(No):
    Ans = None
    Ans = No * No * No
    return Ans

def main():
    Value = None
    Result = None

    print("Enter number : ")
    Value = int(input())

    Result = Cube(Value)

    print("Cube of",Value,"is :",Result)

if __name__ == "__main__":
    main()