'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CheckVowel
//Description:      Check whether character is vowel or not
//Input:            Character
//Output:           Boolean
//Author:           Aaryaa Nandkumar Patil
//Date:             18/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def CheckVowel(ch):
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        return True
    else:
        return False
     
def main():
    cValue = 0
    bRet = False

    cValue = input("Enter character : ")

    bRet = CheckVowel(cValue)

    if bRet == True:
        print(cValue,"is a vowel")
    else:
        print(cValue,"is not a vowel")


if __name__ == "__main__":
    main()