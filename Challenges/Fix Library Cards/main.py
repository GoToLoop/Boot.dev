#!/usr/bin/env python3

class Article:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def card_text(self):
        return self.title + " - " + self.author


class Video:
    def __init__(self, title, minutes):
        self.title = [title]
        self.minutes = minutes

    def minutes_text(self):
        return str(self.minutes) + " min"


def build_library_cards(items):
    cards = []
    for item in items:
        if hasattr(item, "author"):
            cards.append(item.title + " by " + item.author)
        else:
            cards.append("Video: " + item.title[0] + " by " + str(item.minutes))
    return cards



# if __name__ == "__main__":
#     book = LibraryBook("Dune", "Frank Herbert", 2)
#
#     print(book.checkout()) # True
#     print(book.checkout()) # True
#     print(book.checkout()) # False
#     print(book.return_copy()) # True
#
#     print(book.get_status()) # "Dune" by Frank Herbert (0/2 available)
#
#     print(f"{LibraryBook.total_checkouts = }") # LibraryBook.total_checkouts = 2
#     print(f"{book.total_returns = }") # book.total_returns = 1
