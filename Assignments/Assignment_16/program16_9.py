'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    DisplayEven
//Description:      Display first 10 even numbers
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             24/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def DisplayEven():
    for i in range(1,21):
        if i % 2 == 0:
            print(i,end="\t")

def main():        
    DisplayEven()

if __name__ == "__main__":
    main()