'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CheckPerfect
//Description:      Check whether a number is perfect or not
//Input:            Number
//Output:           Boolean
//Author:           Aaryaa Nandkumar Patil
//Date:             19/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def CheckPerfect(No):
    Sum = 0

    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i

    if Sum == No:
        return True
    else:
        return False
    
def main():
    Value = None
    bRet = False

    Value = int(input("Enter number : "))

    bRet = CheckPerfect(Value)

    if bRet == True:
        print(Value,"is perfect number")
    else:
        print(Value,"is not perfect number")

if __name__ == "__main__":
    main()