'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    EvenNum
//Description:      Accept number and print all even numbers till that
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             18/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def EvenNum(No):
    if No < 0:
        return
    
    for i in range(2,No+1):
        if i % 2 == 0:
            print(i)

def main():
    Value = None

    Value = int(input("Enter number : "))

    EvenNum(Value)
    
if __name__ == "__main__":
    main()