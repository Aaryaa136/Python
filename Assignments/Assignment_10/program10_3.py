'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Factorial
//Description:      Print factorial of given number
//Input:            Number
//Output:           Factorial
//Author:           Aaryaa Nandkumar Patil
//Date:             18/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Factorial(No):
    if No < 0:
        return
    
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    Value = None
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = Factorial(Value)
    print("Factorial of",Value,"is :",Ret)
    
if __name__ == "__main__":
    main()