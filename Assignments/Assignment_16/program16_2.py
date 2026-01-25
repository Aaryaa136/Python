'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CheckNum
//Description:      Check whether number is even or odd
//Input:            Number
//Output:           Boolean
//Author:           Aaryaa Nandkumar Patil
//Date:             24/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def CheckNum(No):
    if No % 2 == 0:
        return True
    else:
        return False

def main():
    Value = 0
    bRet = False

    Value = int(input("Enter number : "))

    bRet = CheckNum(Value)

    if bRet == True:
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()