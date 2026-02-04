import os

def main():
    FileName = input("Enter name of the file : ")

    word = "hello"
    count = 0

    if (os.path.exists(FileName)):
        fobj = open(FileName,"r")
        data = fobj.read()
        fobj.close()

        count = data.count(word)

        print("Frequency is : ",count)
                
    else:
        print("File not found")

if __name__ == "__main__":
    main()