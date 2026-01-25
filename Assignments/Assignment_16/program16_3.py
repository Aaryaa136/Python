'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Add
//Description:      Add numbers accepted as parameters
//Input:            Number , Number
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             24/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Add(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Add(Value1,Value2)

    print("Addition is :",Ret)

if __name__ == "__main__":
    main()