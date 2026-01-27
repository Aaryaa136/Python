import threading

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    CountLower , CountUpper , CountDigits
//Description:      Create three threads , count lower , upper case and digits in seperate functions
//Input:            String
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             27/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def CountLower(str1):
    count_small = 0

    for ch in str1:
        if ch >= 'a' and ch <='z':
            count_small = count_small + 1

    print("Number of small letters :",count_small)

def CountUpper(str2):
    count_upper = 0

    for ch in str2:
        if ch >= 'A' and ch <='Z':
            count_upper = count_upper + 1
    
    print("Number of capital letters :",count_upper)

def CountDigits(str3):
    count_digit = 0

    for ch in str3:
        if ch >= '0' and ch <='9':
            count_digit = count_digit + 1
    
    print("Number of digits :",count_digit)
                
def main():
    Name = input("Enter string : ")

    Small = threading.Thread(target=CountLower,args=(Name,))
    Capital = threading.Thread(target=CountUpper,args=(Name,))
    Digits = threading.Thread(target=CountDigits,args=(Name,))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

    print("Exit from main")

if __name__ == "__main__":
    main()