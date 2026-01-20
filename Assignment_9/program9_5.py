'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Divisible_3_5
//Description:      Check whether number is divisible by 3 and 5
//Input:            Number
//Output:           Boolean
//Author:           Aaryaa Nandkumar Patil
//Date:             17/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Divisible_3_5(No):
    if ((No % 3 == 0) and (No % 5 == 0)):
        return True
    else:
        return False

def main():
    Value = None
    Result = None

    print("Enter first number : ")
    Value = int(input())

    Result = Divisible_3_5(Value)

    if(Result == True):
        print(Value,"is divsible by 3 and 5")
    else:
        print(Value,"is not divisible by 3 and 5")

if __name__ == "__main__":
    main()