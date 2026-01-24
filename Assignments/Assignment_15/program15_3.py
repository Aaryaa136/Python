'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Odd
//Description:      Filter odd elements on list, using lamda function using filter
//Input:            List[Numbers]
//Output:           List[Even_nums]
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

    print("Odd elements : ")
    Odd = list(filter(lambda x : x % 2 != 0 ,nums))

    print(Odd)

if __name__ == "__main__":
    main()