'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Divisible_5
//Description:      Check whether number is divisible by 5
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             24/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Divisible_5(No):
    if No % 5 == 0:
        print(No,"is divisible by 5")
    else:
        print(No,"is not divisible by 5")

def main():
    Value = 0

    Value = int(input("Enter number : "))
        
    Divisible_5(Value)

if __name__ == "__main__":
    main()