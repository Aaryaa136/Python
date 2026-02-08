import os

def main():
    FileName = None
    Countlines = 0

    FileName = input("Enter the name of file : ")

    if (os.path.exists(FileName) and os.path.isfile(FileName)):
        fobj = open(FileName,"r")

        Countlines = len(fobj.readlines())

        print("Total number of lines in",FileName," : ",Countlines)
    else:
        print("File does not exists")

if __name__ == "__main__":
    main()