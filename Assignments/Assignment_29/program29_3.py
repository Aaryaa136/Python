import os
import sys

def main():

    if (len(sys.argv[0]) == 1):
        FileNameSrc = input("Enter name of the srource file : ")
   
    fobj = open(FileNameSrc,"r")

    if (os.path.exists(FileNameSrc)):
        Data = fobj.read()

        FileNameDest = input("Enter the source file : ")

        fobjcopy = open(FileNameDest,"w")

        fobjcopy.write(Data)

        print("Data copied successfully")

    else:
        print("File not found")

if __name__ == "__main__":
    main()