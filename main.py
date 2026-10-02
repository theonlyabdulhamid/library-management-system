from library import library, Book, Member


def main():
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
                book = create_book()
                library.add_book(book)
                library.save_books()
                print("Book added successfully")
            elif option == 2:
                x = input("Enter book isbn number: ").strip()
                rbook = library.search_by_isbn(x)
                if rbook == "book not found":
                    print("book not found")
                else:
                    y = library.remove_book(rbook)
                    print(y)

            elif option == 3:
                while True:
                    print(search_menu)
                    try:
                        search_option = int(input("Choose option: "))
                        if search_option == 1:
                            title = input("Enter book tittle: ").strip().title()
                            title_result = library.search_by_title(title)
                            print(title_result)
                            break

                        elif search_option == 2:
                            author = input("Enter book author: ").strip().title()
                            author_result = library.search_by_author(author)
                            print(author_result)
                            break

                        elif search_option == 3:
                            isbn = input("Enter book isbn number: ").strip().title()
                            isbn_result = library.search_by_isbn(isbn)
                            print(isbn_result)
                            break

                        elif search_option == 4:
                            break

                        else:
                            print("Please enter a valid option")
                    except ValueError:
                        print("Please enter a valid option")
            elif option == 4:
                member = create_member()
                library.register_member(member)
                library.save_members()
                print("Member added successfully!")

            elif option == 5:
                res = input("Enter book isbn number: ").strip()
                memb = library.search_member_by_id(input("Enter member id: ").strip())
                if memb == "member not found":
                    print("Member not found")
                else:
                    x = library.borrow_book(memb, book=library.search_by_isbn(res))
                    library.save_members()
                    print(x)

            elif option == 6:
                res = input("Enter book isbn number: ").strip()
                memb = library.search_member_by_id(input("Enter member id: ").strip())
                if memb == "member not found":
                    print("Member not found")
                else:
                    x = library.return_book(memb, book=library.search_by_isbn(res))
                    print(x)

            elif option == 7:
                available = library.view_available_books()
                for index, items in enumerate(available, start=1):
                    print(f"Book {index}:")
                    print(f"Title: {items.title}")
                    print(f"Author: {items.author}")
                    print(f"ISBN: {items.isbn}")
                    print()

            elif option == 8:
                borrowed = library.view_borrowed_books()
                for index, items in enumerate(borrowed, start=1):
                    print(f"Book {index}:")
                    print(f"Title: {items.title}")
                    print(f"Author: {items.author}")
                    print(f"ISBN: {items.isbn}")
                    print()

            elif option == 9:
                print("Goodbye!")
                break

        except ValueError:
            print("Please enter a valid option")


def create_book():
    book_title = input("Book tittle: ").title()
    book_author = input("Book author: ").title()
    book_isbn = input("Book isbn: ")
    book = Book(book_title, book_author, book_isbn)
    return book


def create_member():
    member_name = input("Member name: ").title()
    member_id = input("Member id: ")
    member = Member(member_name, member_id)
    return member

main()
