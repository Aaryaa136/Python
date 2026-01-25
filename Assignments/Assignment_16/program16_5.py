'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    DisplayReverse
//Description:      Display numbers in reverse order
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             24/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def DisplayReverse(No):
    for i in range(No,0,-1):
        print(i,end="\t")

def main():
    Value = 0

    Value = int(input("Enter number : "))

    if Value < 0:
        Value = -Value
        
    DisplayReverse(Value)

if __name__ == "__main__":
    main()