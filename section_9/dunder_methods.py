from typing import Self


class Book:
    def __init__(self, title: str, pages: int) -> None:
        self.title = title
        self.pages = pages

    def __len__(self) -> int:
        return self.pages

    def __add__(self, other: Self) -> Self:
        combined_title: str = self.title + " " + other.title
        combined_pages: int = self.pages + other.pages
        # This is a way to return the same class type.
        # This is important because if you return a different class type, you will not be able to use the dunder methods of the class
        return type(self)(combined_title, combined_pages)

def main() -> None:
    py_daily: Book = Book("PyDaily", 100)
    harry_potter: Book = Book("Harry Potter", 340)
    print(len(py_daily)) # This will print the number of pages in the book
    print(len(harry_potter)) # This will print the number of pages in the book

    # this is not supported without the __add__ dunder method
    combined_books: Book = py_daily + harry_potter
    print(combined_books.title)
    print(combined_books.pages)

    # Another way to get it is to use the dunder method
    # print(py_daily.__len__()) # this is not recommended

if __name__ == '__main__':
    main()
