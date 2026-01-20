'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Sum_N
//Description:      Display sum of first N natural numbers
//Input:            Number
//Output:           Sum
//Author:           Aaryaa Nandkumar Patil
//Date:             18/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Sum_N(No):
    if No < 0:
        return
    
    Sum = 0

    for i in range(1,No+1):
        Sum = Sum + i

    return Sum

def main():
    Value = None
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = Sum_N(Value)
    print("Sum of n natural number is : ",Ret)
    
if __name__ == "__main__":
    main()