#!/usr/bin/env python3

class LibraryBook:
    total_checkouts = 0
    total_returns = 0

    def __init__(self, title: str, author: str, total_copies: int):
        if total_copies < 0: raise ValueError("total_copies can't be negative!")

        self.title = title
        self.author = author
        self.__available_copies = self.total_copies = total_copies


    def checkout(self) -> bool:
        if self.__available_copies <= 0: return False

        self.__available_copies -= 1
        LibraryBook.total_checkouts += 1

        return True


    def return_copy(self) -> bool:
        if self.__available_copies >= self.total_copies: return False

        self.__available_copies += 1
        LibraryBook.total_returns += 1

        return True


    def get_status(self) -> str:
        return '"%s" by %s (%d/%d available)' % (
            self.title, self.author, self.__available_copies, self.total_copies
        )


    def get_available_copies(self) -> int: return self.__available_copies



if __name__ == "__main__":
    book = LibraryBook("Dune", "Frank Herbert", 2)

    print(book.checkout()) # True
    print(book.checkout()) # True
    print(book.checkout()) # False
    print(book.return_copy()) # True

    print(book.get_status()) # "Dune" by Frank Herbert (0/2 available)

    print(f"{LibraryBook.total_checkouts = }") # LibraryBook.total_checkouts = 2
    print(f"{book.total_returns = }") # book.total_returns = 1
