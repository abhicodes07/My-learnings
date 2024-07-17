class Library:
    def __init__(self):
        self.books = []
        print("The Library is empty, Please Added some books!")
        print()
        self.addBooks()
        
    def allBooks(self):
        print()
        print("-- Welcome to the Libray! --")
        while True:
            print("\nPlease select an option: \n\t1. Show all books\n\t2. Add books\n\t3. Show number of books\n\t4. Exit")
            self.option = int(input("Enter the option: "))
            match self.option:
                case 1:
                    print()
                    self.printBooks()
                case 2:
                    print()
                    self.addBooks()
                case 3:
                    print()
                    print(f"The number of available books in Library: {self.numBooks()}")
                case 4:
                    return False

    def printBooks(self):
        for index, value in enumerate(self.books, start=1):
            print(f"\t{index}. {value}")
        print("The Number of available books: ", self.numBooks())
        print()
        
    def addBooks(self):
        new_book = input("Enter the name of the Book: ")
        self.books.append(new_book)
        print("Book successfully added!")
        prompt = input("Do you want add more books (y/n): ")
        
        match prompt:
            case 'y':
                prompt1 = int(input("Enter the number of books you want to add: "))
                for _ in range(prompt1):
                    prompt2 = input(f"Enter the name of the {_} book: ")
                    self.books.append(prompt2)
                    print("Book successfully added!")
                    print()
            case 'n':
                print("Okay! Here are the available books.")
                print()
                self.printBooks()

    def numBooks(self):
        return len(self.books)
        
user = Library()
user.allBooks()


