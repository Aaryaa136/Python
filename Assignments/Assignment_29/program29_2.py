import os

def main():
    FileName = input("Enter name of the file : ")

    if (os.path.exists(FileName)):
        fobj = open(FileName,"r")

        Data = fobj.read()
        print(Data)

    else:
        print("File not found")

if __name__ == "__main__":
    main()