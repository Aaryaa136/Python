'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Display
//Description:      Accept 1 number and print from 1 to N
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             18/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def Display(No):
    if No < 0:
        No = -No
    for i in range(1,No+1):
        print(i,end="\t")
  
def main():
    Value = 0

    Value = int(input("Enter number : "))

    Display(Value)

if __name__ == "__main__":
    main()