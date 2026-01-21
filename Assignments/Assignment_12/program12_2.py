'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    DisplayFactors
//Description:      Display factors of given number
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             18/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def DisplayFactors(No):
    print("Factors of",No,":")
    for i in range(1,No):
        if No % i == 0:
            print(i)
  
def main():
    Value = 0

    Value = int(input("Enter number : "))

    DisplayFactors(Value)

if __name__ == "__main__":
    main()