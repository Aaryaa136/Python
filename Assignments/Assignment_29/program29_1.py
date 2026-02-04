import os

def main():
    FileName = input("Enter name of the file : ")

    if (os.path.exists(FileName)):
        print("File is present")
    else:
        print("File not found")

if __name__ == "__main__":
    main()