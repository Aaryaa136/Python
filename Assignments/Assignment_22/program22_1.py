'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    fun() , gun()
//Description:      Create class having above method : create 2 objects and invoke 
//Input:            Number , Number
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             28/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class Demo:
    Value = 13

    def __init__(self,Value1,Value2):
        self.No1 = Value1
        self.No2 = Value2
    
    def fun(self):
        print(self.No1,self.No2)

    def gun(self):
        print(self.No1,self.No2)

def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.fun()
    obj2.fun()

    obj1.gun()
    obj2.gun()

if __name__ == "__main__":
    main()