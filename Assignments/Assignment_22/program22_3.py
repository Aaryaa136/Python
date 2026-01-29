'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Accept() , Addition() , Substraction() , Multiplication() , Division()
//Description:      Create class having above method : perform basic arithmetci calculations like , add, sub , multiply and divide
//Input:            Nothing , Number , Number , Number , Number
//Output:           Nothing , Number , Number , Number , Number
//Author:           Aaryaa Nandkumar Patil
//Date:             28/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Aceept(self):
        self.Value1 = int(input("Enter first number : "))
        self.Value2 = int(input("Enter second number : "))

    def Addition(self):
        Ans = 0
        Ans = self.Value1 + self.Value2
        return Ans
    
    def Substracton(self):
        Ans = 0
        Ans = self.Value1 - self.Value2
        return Ans
      
    def Multiplication(self):
        Ans = 0
        Ans = self.Value1 * self.Value2
        return Ans
       
    def Division(self):
        Ans = 0
        Ans = self.Value1 / self.Value2
        return Ans

def main():
    Ret = 0

    obj1 = Arithmetic()
    obj2 = Arithmetic()
    obj3 = Arithmetic()

    obj1.Aceept()

    Ret = obj1.Addition()
    print("Addition is :",Ret)
  
    Ret = obj1.Substracton()
    print("Substraction is :",Ret)

    Ret = obj1.Multiplication()
    print("Multiplication is :",Ret)
        
    Ret = obj1.Division()
    print("Division is :",Ret)

    print("")

    obj2.Aceept()

    Ret = obj2.Addition()
    print("Addition is :",Ret)
  
    Ret = obj2.Substracton()
    print("Substraction is :",Ret)

    Ret = obj2.Multiplication()
    print("Multiplication is :",Ret)
        
    Ret = obj2.Division()
    print("Division is :",Ret)

    print("")

    obj3.Aceept()

    Ret = obj3.Addition()
    print("Addition is :",Ret)
  
    Ret = obj3.Substracton()
    print("Substraction is :",Ret)

    Ret = obj3.Multiplication()
    print("Multiplication is :",Ret)
        
    Ret = obj3.Division()
    print("Division is :",Ret)


if __name__ == "__main__":
    main()