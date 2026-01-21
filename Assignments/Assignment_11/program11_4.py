'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    ReverseDigits
//Description:      Accept number and print it in reverse order
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def ReverseDigits(No):
    Digit = 0

    if No < 0:
        No = -No 

    print("Reverse order is : ")
    while (No != 0):
        Digit = No % 10
        print(Digit,end="")
        No = No // 10
      
def main():
    Value = None

    Value = int(input("Enter number : "))

    ReverseDigits(Value)

if __name__ == "__main__":
    main()


#Reverse = Reverse * 10 + Digit