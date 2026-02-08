import os

def main():
    FileName = None

    FileName = input("Enter the name of file : ")

    if (os.path.exists(FileName) and os.path.isfile(FileName)):
        fobj = open(FileName,"r")

        data = fobj.readlines()
        
        for i in data:
            print(i)

    else:
        print("File does not exists")

if __name__ == "__main__":
    main()