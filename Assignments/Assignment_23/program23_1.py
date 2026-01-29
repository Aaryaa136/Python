class BookStore:
    NoOfBooks = 0

    def __init__(self,Book,Person):
        self.Name = Book
        self.Author = Person
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.Name,"by",self.Author)
        print("No of books :",BookStore.NoOfBooks)

def main():
    obj1 = BookStore("Linux System Programming","Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming","Dennis Ritchie")
    obj2.Display()

    obj3 = BookStore("Thinking in C++","Bruce Eckel")
    obj3.Display()

if __name__ == "__main__":
    main()