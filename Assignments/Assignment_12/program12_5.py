
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    DisplayReverse
//Description:      Accept 1 number and print from 1 to N in reverse order
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             18/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def DisplayReverse(No):
    if No < 0:
        No = -No
    for i in range(No,0,-1):
        print(i,end="\t")
  
def main():
    Value = 0

    Value = int(input("Enter number : "))

    DisplayReverse(Value)

if __name__ == "__main__":
    main()