'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    String5
//Description:      Return list of string having length more than 5, using lamda function using filter
//Input:            List
//Output:           List
//Author:           Aaryaa Nandkumar Patil
//Date:             24/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def main():
    Size = 0
    str = 0
    nums = list()

    Size = int(input("Enter number of elements : "))

    if Size < 0:
        Size = -Size

    print("Enter elements : ")
    for i in range(Size):
        str = input()
        nums.append(str)

    print("")
    String5 = list(filter(lambda strX : len(strX) > 5 ,nums))

    print(String5)

if __name__ == "__main__":
    main()