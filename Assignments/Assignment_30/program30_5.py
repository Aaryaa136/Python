import os

def main():
    FileName = None
    Word = None

    FileName = input("Enter the name of file : ")

    Word = input("Enter the word : ")
    

    if (os.path.exists(FileName) and os.path.isfile(FileName)):
        fobj = open(FileName,"r")

        data = fobj.read()
        words = data.split()

        if Word in words:
            print("Word present in file")
        else:
            print("Word not found in file")
    else:
        print("File does not exists")

if __name__ == "__main__":
    main()