'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    FactSummation
//Description:      Return addition of factors
//Input:            Number 
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def FactSummation(No):
    sum = 0

    for i in range(1,No):
        if No % i == 0:
            print(i)
            sum = sum + i

    return sum

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter number : "))

    if Value < 0:
        Value = -Value

    Ret = FactSummation(Value)

    print("Summation of factors of",Value,"is :",Ret)

if __name__ == "__main__":
    main()