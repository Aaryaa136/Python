'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Pattern
//Description:      1   2   3
//                  1   2   3
//                  1   2   3    
//Input:            Number 
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             25/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def Pattern(No):
    for i in range(1,No+1):
        for j in range(1,No+1):
                print(j,end="\t")

        print("")

def main():
    Value = 0

    Value = int(input("Enter number : "))

    if Value < 0:
        Value = -Value

    Pattern(Value)

if __name__ == "__main__":
    main()