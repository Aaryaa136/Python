'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    AreaRectangle
//Description:      Calculate area of rectangle
//Input:            Length , Width
//Output:           Area
//Author:           Aaryaa Nandkumar Patil
//Date:             19/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def AreaRect(length,width):
    if length < 0:
        length = -length

    if width < 0:
        width = -width

    area = None
    area = length * width
    return area

def main():
    Value1 = None
    Value2 = None
    Ret = None

    Value1 = int(input("Enter length : "))
    Value2 = int(input("Enter width : "))

    Ret = AreaRect(Value1,Value2)

    print("Area of rectangle is : ",Ret)

if __name__ == "__main__":
    main()