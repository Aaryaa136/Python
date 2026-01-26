'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Factorial
//Description:      Find factorial of a given number
//Input:            Number 
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Factorial(No):
    fact = 1

    for i in range(1,No+1):
        fact = fact * i

    return fact

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    if Value < 0:
        Value = -Value

    Ret = Factorial(Value)

    print("Factorial is :",Ret)

if __name__ == "__main__":
    main()