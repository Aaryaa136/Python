import threading

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    EvenRange , OddRange
//Description:      Create two threads display , first 10 even numbers and first 10 odd numbers
//Input:            Nothing
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             27/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def EvenRange():
    print("First 10 even elements : ")
    for i in range(1,21):
        if i % 2 == 0:
            print(i,end="\t")
    print("")

def OddRange():
    print("First 10 odd elements : ")
    for i in range(1,20):
        if i % 2 != 0:
            print(i,end="\t")

    print("")

def main():
    t1 = threading.Thread(target=EvenRange)
    t2 = threading.Thread(target=OddRange)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()