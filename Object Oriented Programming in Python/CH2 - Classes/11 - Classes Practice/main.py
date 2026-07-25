from dataclasses import dataclass, astuple

@dataclass
class Book: title: str; author: str

class Library:
    def __init__(lib, name: str):
        lib.name = name
        lib.books: list[Book] = []


    def add_book(lib, book: Book): lib.books.append(book)


    def remove_book(lib, book: Book):
        while book in lib.books: lib.books.remove(book)


    def search_books(lib, search: str) -> list[Book]:
        search = search.lower()

        return [
            book for book in lib.books
            if any( search in name for name in map(str.lower, astuple(book)) )
            # if search in book.title.lower() or search in book.author.lower()
        ]
