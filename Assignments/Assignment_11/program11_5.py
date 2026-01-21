'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CheckPalindrome
//Description:      Check whether number is palindrome or not
//Input:            Number
//Output:           Boolean
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def CheckPalindrome(No):
    Digit = 0
    Reverse = 0

    if No < 0:
        No = -No 

    temp = No
    
    while (No != 0):
        Digit = No % 10
        Reverse = (Reverse*10) + Digit
        No = No // 10

    if temp == Reverse:
        return True
    else:
        return False
      
def main():
    Value = None
    bRet = False

    Value = int(input("Enter number : "))

    bRet = CheckPalindrome(Value)

    if bRet == True:
        print("It is palindrome number")
    else:
        print("Not palindrome number")
if __name__ == "__main__":
    main()


#Reverse = Reverse * 10 + Digit
#we are storing in another variable caz No gets 0 , after extracting 