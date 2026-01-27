import threading

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    EvenFactorSum , OddFactorSum
//Description:      Create two threads , adding even factors and odd factors 
//Input:            Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             27/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def EvenFactorSum(No):
    sum_even = 0

    for i in range(1,No+1):
        if No % i == 0 and i % 2 == 0:
            sum_even = sum_even + i
            
    print("Sum of even factors :",sum_even)

def OddFactorSum(No):
    sum_odd = 0

    for i in range(1,No+1):
        if No % i == 0 and i % 2 != 0:
            sum_odd = sum_odd + i
    
    print("Sum of odd factors :",sum_odd)
                
def main():
    Value = 0

    Value = int(input("Enter number : "))

    t1 = threading.Thread(target=EvenFactorSum,args=(Value,))
    t2 = threading.Thread(target=OddFactorSum,args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()