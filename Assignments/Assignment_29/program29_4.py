import sys
import os

def main():
    if(len(sys.argv) != 3):
        print("Enter valid command")

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if(os.path.isfile(file1) and os.path.isfile(file2)):
        fobj1 = open(file1,"r+b")
        fobj2 = open(file2,"r+b")

        data1 = fobj1.read()
        data2 = fobj2.read()

        fobj1.close()
        fobj2.close()

        if len(data1) == len(data2):
            print("Success")
        else:
            print("Failure")
    else:
        print("File not found")
    
if __name__ == "__main__":
    main()
