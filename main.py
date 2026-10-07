from library import library, Book, Member


def main():
    library.load_books()
    library.load_members()
    menu = """
========================================
          LIBRARY MANAGEMENT SYSTEM
========================================

1. Add book
2. Remove book
3. Search for book
4. Register member
5. Borrow book
6. Return book
7. View available books
8. View borrowed books
9. Exit
"""
    search_menu = """
========================================
             SEARCH BOOK
========================================

1. Search by title
2. Search by author
3. Search by ISBN
4. Back to main menu"""

    while True:
        print(menu)
        try:
            option = int(input("Choose an option: "))
            if option == 1:
                book, success = create_book()
                if success:
                    library.add_book(book)
                    print("Book added successfully")
                else:
                    print(book)
            elif option == 2:
                isbn_number = input("Enter book isbn number: ").strip()
                book = library.search_by_isbn(isbn_number)
                if book is None:
                    print("book not found")
                else:
                    result = library.remove_book(book)
                    print(result)

            elif option == 3:
                while True:
                    print(search_menu)
                    try:
                        search_option = int(input("Choose option: "))
                        if search_option == 1:
                            title = input("Enter book tittle: ").strip().title()
                            title_result = library.search_by_title(title)
                            if title_result is None:
                                print("book not found")
                            else:
                                print(title_result)
                            break

                        elif search_option == 2:
                            author = input("Enter book author: ").strip().title()
                            author_result = library.search_by_author(author)
                            if author_result is None:
                                print("Book not found")
                            else:
                                print(author_result)
                            break

                        elif search_option == 3:
                            isbn = input("Enter book isbn number: ").strip().title()
                            isbn_result = library.search_by_isbn(isbn)
                            if isbn_result is None:
                                print("Book not found")
                            else:
                                print(isbn_result)
                            break

                        elif search_option == 4:
                            break

                        else:
                            print("Please enter a valid option")
                    except ValueError:
                        print("Please enter a valid option")
            elif option == 4:
                member, success = create_member()
                if success:
                    library.register_member(member)
                    print("Member added successfully!")
                else:
                    print(member)

            elif option == 5:
                isbn = input("Enter book isbn number: ").strip()
                member = library.search_member_by_id(input("Enter member id: ").strip())
                if member is None:
                    print("Member not found")
                else:
                    book=library.search_by_isbn(isbn)
                    if book is None:
                        result = library.borrow_book(
                            member, book
                        )
                        print(result)

            elif option == 6:
                isbn = input("Enter book isbn number: ").strip()
                book = library.search_by_isbn(isbn)

                member = library.search_member_by_id(input("Enter member id: ").strip())
                if member is None:
                    print("Member not found")
                else:
                    if book is None:
                        print("book not found")
                    else:
                        return_book = library.return_book(member, book)
                        print(return_book)

            elif option == 7:
                available = library.view_available_books()
                for index, book in enumerate(available, start=1):

                    print(f"Book {index}:")
                    print(book)
                    print()

            elif option == 8:
                borrowed = library.view_borrowed_books()
                for index, book in enumerate(borrowed, start=1):
                    print(f"Book {index}:")
                    print(book)
                    print()

            elif option == 9:
                library.save_books()
                library.save_members()
                print("Goodbye!")
                break

        except ValueError:
            print("Please enter a valid option")


def create_book():
    book_title = input_validation("Book tittle").title()
    book_author = input_validation("Book author").title()
    book_isbn = input_validation("Book isbn")
    if not library.search_by_isbn(book_isbn):
        return Book(book_title, book_author, book_isbn), True
    else:
        return "Book ISBN already exists", False


def create_member():
    member_name = input_validation("Member name").title()
    member_id = input_validation("Member id")
    if library.search_member_by_id(member_id) is None:
        member = Member(member_name, member_id), True
        return member
    else:
        return "Member id already exists", False


def input_validation(prompt):
    while True:
        valid = input(f"{prompt}: ").strip()
        if valid:
            return valid
        else:
            print("Empty input not allowed")


main()
