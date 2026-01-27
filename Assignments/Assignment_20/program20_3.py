import threading

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    EvenList , OddList
//Description:      Create two threads , extract all even elements and sum it and extract all odd elements and sum it 
//Input:            List , Size
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             27/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def EvenList(arr,size):
    sum_even = 0

    for i in range(size):
        if arr[i] % 2 == 0:
            sum_even = sum_even + arr[i]
            
    print("Sum of even factors :",sum_even)

def OddList(brr,size):
    sum_odd = 0

    for i in range(size):
        if brr[i] % 2 != 0:
            sum_odd = sum_odd + brr[i]
    
    print("Sum of odd factors :",sum_odd)
                
def main():
    length = 0
    Value = 0
    nums = []

    length = int(input("Enter number of elements : "))

    for i in range(length):
        Value = int(input())
        nums.append(Value)

    t1 = threading.Thread(target=EvenList,args=(nums,length))
    t2 = threading.Thread(target=OddList,args=(nums,length))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()