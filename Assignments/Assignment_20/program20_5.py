import threading

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Display , DisplayReverse
//Description:      Create two threads , using synchronization : thread should wait till first thread completes execution
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             27/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

i = 0
lobj = threading.Lock()

def Display():
    print("Linear order :")
    global i

    for i in range(1,51):
        with lobj:
            print(i,end="\t")

    print("")

def DisplayReverse():
    print("Reverse order : ")
    global i
    for i in range(50,0,-1):
        with lobj:
            print(i,end="\t")

    print("")

def main():
    t1 = threading.Thread(target=Display)
    t2 = threading.Thread(target=DisplayReverse)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
if __name__ == "__main__":
    main()