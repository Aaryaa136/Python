'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    PowerTwo
//Description:      Return power of two using lambda function
//Input:            Number
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             26/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

PowerTwo = lambda No : No ** 2

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = PowerTwo(Value)

    print(Value,"power two is :",Ret)


if __name__ == "__main__":
    main()