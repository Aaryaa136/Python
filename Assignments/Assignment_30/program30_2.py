import os

def main():
    FileName = None
    Countwords = 0

    FileName = input("Enter the name of file : ")

    if (os.path.exists(FileName) and os.path.isfile(FileName)):
        fobj = open(FileName,"r")

        data = fobj.read()
        words = data.split()       # split strings into words

        Countwords = len(words)

        print("Total number of words in",FileName," : ",Countwords)
    else:
        print("File does not exists")

if __name__ == "__main__":
    main()