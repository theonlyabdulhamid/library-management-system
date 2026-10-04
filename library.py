import json


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def search_by_title(self, title):

        for book in self.books:
            if book.title == title:
                return book
        return "book not found"

    def search_by_author(self, author):

        for book in self.books:
            if book.author == author:
                return book
        return "book not found"

    def search_by_isbn(self, isbn):

        for book in self.books:
            if book.isbn == isbn:
                return book
        return "book not found"

    def remove_book(self, book):
        try:
            x = self.books.index(book)
            self.books.pop(x)
            return "Book removed!"
        except ValueError:
            return "Book not found"

    def borrow_book(self, member, book):
        if book not in self.books:
            return "Book not found"
        if member not in self.members:
            return "Not a Registered member"
        if not book.available:
            return "Book is not available"
        book.available = False
        member.borrowed_books.append(book)
        return "Book Borrowed successfully"

    def return_book(self, member, book):
        if member not in self.members:
            return "Only a registered member have access to return a book"
        if book not in member.borrowed_books:
            return "You didnt borrow this book"
        book.available = True
        x = member.borrowed_books.index(book)
        member.borrowed_books.pop(x)
        return "Book returned successfully"

    def view_available_books(self):
        available_books = []
        for book in self.books:
            if book.available:
                available_books.append(book)
        return available_books

    def view_borrowed_books(self):
        borrowed = []
        for member in self.members:
            borrowed.extend(member.borrowed_books)
        return borrowed

    def search_member_by_id(self, id):
        for member in self.members:
            if member.member_id == id:
                return member
        return "member not found"

    def save_books(self):
        books_data = []
        for book in self.books:
            book_data = {
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "available": book.available,
            }
            books_data.append(book_data)
        with open("books.json", "w") as file:
            json.dump(books_data, file, indent=4)

    def save_members(self):
        members_data = []

        for member in self.members:
            borrowed_isbn = []
            for l in member.borrowed_books:
                borrowed_isbn.append(l.isbn)

            member_data = {
                "member name": member.name,
                "member id": member.member_id,
                "borrowed bookd isbn": borrowed_isbn,
            }
            members_data.append(member_data)
        with open("members.json", "w") as file:
            json.dump(members_data, file, indent=3)

    def load_books(self):
        self.books = []
        with open("books.json") as file:
            books_data = json.load(file)
        for book in books_data:
            book_title = book["title"]
            book_author = book["author"]
            book_isbn = book["isbn"]
            book_availability = book["available"]
            book = Book(book_title, book_author, book_isbn)
            book.available = book_availability
            self.books.append(book)

    def load_members(self):
        self.members = []
        with open("members.json") as file:
            members_data = json.load(file)
        for libmember in members_data:
            member_name = libmember["member name"]
            member_id = libmember["member id"]
            member = Member(member_name, member_id)
            self.members.append(member)
            borrowed_isbn=libmember["borrowed bookd isbn"]
            member.borrowed_books=[]
            for borrowed in borrowed_isbn:
                member.borrowed_books.append(self.search_by_isbn(borrowed))


library = Library()
