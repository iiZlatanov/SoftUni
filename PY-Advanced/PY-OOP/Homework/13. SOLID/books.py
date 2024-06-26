from typing import List


class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books: List[str] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def find_book(self, title) -> str:
        if title in self.books:
            return title.title()
        else:
            return "No such book in the library"
