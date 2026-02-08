import os

def main():
    FileNameSrc = None
    FileNameDest = None

    FileNameSrc = input("Enter the name of source file : ")
    FileNameDest = input("Enter the name of destination file : ")

    if (os.path.exists(FileNameSrc) and os.path.isfile(FileNameSrc)):
        fobjsrc = open(FileNameSrc,"r")

        data = fobjsrc.read()

        fobjdest = open(FileNameDest,"w")
        fobjdest.write(data)

        print("File copied sucessfully")
        
    else:
        print("Source file does not exists")

if __name__ == "__main__":
    main()