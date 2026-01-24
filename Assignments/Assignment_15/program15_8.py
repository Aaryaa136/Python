'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Divisible_3_5
//Description:      Return list of numbers which are divisible by 3 and 5, using lamda function using filter
//Input:            List[Numbers]
//Output:           Number
//Author:           Aaryaa Nandkumar Patil
//Date:             24/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def main():
    Size = 0
    Value = 0
    nums = list()

    Size = int(input("Enter number of elements : "))

    if Size < 0:
        Size = -Size

    print("Enter elements : ")
    for i in range(Size):
        Value = int(input())
        nums.append(Value)

    print("Elements which are divisible by 5 and 3 : ")
    Divisible_3_5 = list(filter(lambda x : x % 3 == 0 and Value % 5 == 0 ,nums))

    print(Divisible_3_5)

if __name__ == "__main__":
    main()