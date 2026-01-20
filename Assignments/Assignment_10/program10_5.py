'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    OddNum
//Description:      Accept number and print all odd numbers till that
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             18/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def OddNum(No):
    if No < 0:
        return
    
    for i in range(1,No+1):
        if i % 2 != 0:
            print(i)

def main():
    Value = None

    Value = int(input("Enter number : "))

    OddNum(Value)
    
if __name__ == "__main__":
    main()