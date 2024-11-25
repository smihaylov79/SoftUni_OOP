from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        return book.content


class A4Formatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content[:-2]


class Printer:
    def get_book(self, formatter: Formatter, book: Book):
        return formatter.format(book)
