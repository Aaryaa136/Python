'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    AreaCircle
//Description:      Calculate area of circle
//Input:            Radius
//Output:           Area
//Author:           Aaryaa Nandkumar Patil
//Date:             19/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

PI = 3.14

def AreaCircle(radius):
    if radius < 0:
        radius = -radius

    global PI

    area = 0
    area = PI * radius * radius

    return area

def main():
    Value1 = None
    Ret = None

    Value = int(input("Enter radius : "))

    Ret = AreaCircle(Value)

    print("Area of circle is : ",Ret)

if __name__ == "__main__":
    main()