'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Display
//Description:      Display pattern : *
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             24/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Display(No):
    for i in range(No):
        print("*",end="\t")

def main():
    Value = 0

    Value = int(input("Enter number : "))

    if Value < 0:
        Value = -Value
        
    Display(Value)

if __name__ == "__main__":
    main()