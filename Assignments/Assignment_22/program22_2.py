'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    Accept() , CalculateArea() , CalculateCircumference
//Description:      Create class having above method : whic calculates aread and circumference of circle
//Input:            Nothing
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             28/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius : ")) 

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
    
    def CalculateCircumferece(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius is :",self.Radius)
        print("Area of circle is :",self.Area)
        print("Circumference of circle is :",self.Circumference)

def main():
    obj1 = Circle()
    obj2 = Circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumferece()
    obj1.Display()

    print("")
    
    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumferece()
    obj2.Display()

if __name__ == "__main__":
    main()