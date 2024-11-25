class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def edit_book(self, title, author, new_title):
        book=[b for b in self.books if b.title == title and b.author==author][0]
        book.title = new_title

    def find_book(self, title):
        try:
            return [b for b in self.books if b.title==title][0]
        except:
            return 'No such book!'
