'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Table
//Description:      Print table of given number
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             18/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Table(No):
    if No < 0:
        No = -No

    for i in range(1,11):
        print(No*i)

def main():
    Value = None

    Value = int(input("Enter number : "))

    Table(Value)
    
if __name__ == "__main__":
    main()