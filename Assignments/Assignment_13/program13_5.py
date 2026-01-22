'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//
//Function Name:    DisplayGrades
//Description:      Based on marks display grade
//Input:            Marks
//Output:           Nothing
//Author:           Aaryaa Nandkumar Patil
//Date:             19/1/26
//
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def DisplayGrade(Marks):
    if Marks < 0:
        print("Please enter valid marks")
        return
    
    if Marks >= 75:
        print("Distinction")
    elif Marks >= 60:
        print("First class")
    elif Marks >= 50:
        print("Second class")
    else:
        print("Fail")
    
def main():
    Value = None

    Value = int(input("Enter marks  : "))

    DisplayGrade(Value)

if __name__ == "__main__":
    main()