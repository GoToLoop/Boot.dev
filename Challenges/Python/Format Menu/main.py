#!/usr/bin/env python3

def format_menu(menu: dict[str, int]) -> str:
    return '\n'.join( food + f" - ${price}" for food, price in menu.items() )


if __name__ == "__main__":
    menu = { "Burger": 5, "Fries": 3, "Soda": 2 }
    print(format_menu(menu)) # "Burger - $5\nFries - $3\nSoda - $2"

    empty: dict[str, int] = {}
    print(format_menu(empty)) # ""
