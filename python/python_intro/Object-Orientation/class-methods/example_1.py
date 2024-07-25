class Book:
    COUNT = 0
    def __init__(self, title: str, author: str) -> str:
        self.title = title
        self.author = author
        Book.COUNT += 1
    @classmethod
    def count(cls):
        print(f"Number of books available: {cls.COUNT}")

book1: object = Book("Reasoning", "Agarwal")
book2: object = Book("Roget's Thesuarus", "Roget")
book1.count()
book2.count()
book3 = Book("Crime & punishment", "Dostoyevesky")
book3.count()
