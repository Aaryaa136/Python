'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CheckGreater
//Description:      check greater among two numbers
//Input:            Number , Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             17/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def CheckGreater(No1,No2):
    if No1 > No2:
        print(No1,"is greater")
    else:
        print(No2,"is greater")

def main():
    Value1 = None
    Value2 = None

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    CheckGreater(Value1,Value2)

if __name__ == "__main__":
    main()