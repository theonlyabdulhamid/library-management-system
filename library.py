class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow(self): ...
    def return_book(self): ...


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrowed_books(): ...
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
        available_books=[]
        for book in self.books:
            if book.available:
                available_books.append(book)
        return available_books
    def view_borrowed_books(self):
        borrowed=[]
        for member in library.members:
                borrowed.extend(member.borrowed_books)
        return borrowed

library = Library()
# book1 = Book("Atomic Habits", "James Clear", "9780735211292")  # object1
# book2 = Book("Clean Code", "Robert C. Martin", "9780132350884")  # object2
# book3 = Book("The Alchemist", "Paulo Coelho", "9780061122415")  # object3
# book4 = Book("Python Crash Course", "Eric Matthes", "9781593279288")
# books = [book1, book2, book3, book4]

# for book in books:
#     library.add_book(book)

# member1 = Member("Abdulhamid", "M001")
# member2 = Member("Larry", "M002")
# member3 = Member("Abdulbasit", "M003")
# member1.borrowed_books.append(book1)
# member4 = Member("Aisha", "M004")
# members = [member1, member2, member3, member4]


# for i in members:
#     library.register_member(i)
# library.remove_book(book4)

# # print(library.borrow_book(member1, book1))
# # print(book1.available)
# # print(member1.borrowed_books[0].title)
# # print(library.return_book(member1, book1))
# # print(book1.available)
# borrowed = library.view_borrowed_books()

# for book in borrowed:
#     print(book.title)