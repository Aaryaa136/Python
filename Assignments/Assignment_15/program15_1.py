'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Square
//Description:      Find square of number on a list, using lamda function using map
//Input:            List[Numbers]
//Output:           List[Squares]
//Author:           Aaryaa Nandkumar Patil
//Date:             23/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def main():
    Size = 0
    Value = 0
    nums = []      # nums = list()

    Size = int(input("Enter number of elements : "))

    if Size < 0:
        Size = -Size

    print("Enter elements : ")
    for i in range(Size):
        Value = int(input())
        nums.append(Value)

    print("Square is : ")
    Square = list(map(lambda x : x**2,nums))

    print(Square)

if __name__ == "__main__":
    main()