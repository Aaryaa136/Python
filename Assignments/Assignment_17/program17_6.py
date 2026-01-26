
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Pattern
//Description:      *   *   *
//                  *   *  
//                  *        
//Input:            Number 
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def Pattern(No):
    for i in range(1,No+1):
        for j in range(1,No+1):
            if j >= i:
                print("*",end="\t")

        print("")

def main():
    Value = 0

    Value = int(input("Enter number : "))

    if Value < 0:
        Value = -Value

    Pattern(Value)

if __name__ == "__main__":
    main()