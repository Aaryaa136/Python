'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    FindLargest
//Description:      Find largest among three numbers, using lamda
//Input:            Number , Number , Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             21/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

FindLargest = lambda No1,No2,No3 : No1 if(No1>No2 and No1>No3) else(No2 if No2>No3 else No3)  

def main():
    Value1 = None
    Value2 = None
    Value3 = None
    Ret = 0

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    Value2 = int(input("Enter third number : "))

    Ret = FindLargest(Value1,Value2,Value3) 

    if Ret == Value1:
        print(Value1,"is greater")  
    elif Ret == Value2:
        print(Value2,"is greater") 
    else:
        print(Value3,"is greater")    

if __name__ == "__main__":
    main()