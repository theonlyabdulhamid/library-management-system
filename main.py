from library import library,Book,Member

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
    search_menu="""
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
            if option==1:
                book=create_book()
                library.add_book(book)
                print("Book added successfully")
            elif option==2:
                library.remove_book()
            elif option==3:  
                while True:
                    print(search_menu)
                    try: 
                        search_option= int(input("Choose option"))
                        if search_option==1:
                            library.search_by_title
                            break
                        elif search_option==2:
                            library.search_by_author
                            break
                        elif search_option==3:
                            library.search_by_isbn
                            break
                        elif search_option==4:
                            break
                        else:
                            print("Please enter a valid option")
                    except ValueError:
                        print("Please enter a valid option")
            elif option==4:
                library.register_member()
            elif option==5:
                library.borrow_book()
            elif option==6:
                library.return_book()
            elif option==7:
                library.view_available_books()
            elif option==8:
                library.view_borrowed_books()
            elif option==9:
                print("Goodbye!")
                break
        except ValueError:
            print("Please enter a valid option")
def create_book():
    book_title=input("Book tittle: ").title()
    book_author=input("Book author: ").title()
    book_isbn=input("Book isbn: ")
    book=book_title,book_author,book_isbn
    return book

main()
