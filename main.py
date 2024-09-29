from project_setup import project_setup
from constants import MAIN_MENU, LIBRARY_MENU, ADMIN_MENU
from db_tools import *
from csv_tools import *
from book import Book

project_setup()

# Declarando variável de opção e atribuindo valor arbitrário para entrar no laço while
option_main = 0

while option_main != 3:
    print(MAIN_MENU)
    option_main = int(input("Insert option number: "))

    match option_main:
        case 1:
            # Declarando variável de opção e atribuindo valor arbitrário para entrar no laço while
            option_library = 0

            while option_library != 6:
                print(LIBRARY_MENU)
                option_library = int(input("Insert option number: "))

                match option_library:
                    case 1:
                        title = input("\nTitle: ")
                        author = input("Author: ")
                        price = input("Price: ")
                        pub_year = input("Publication Year: ")

                        add_book(Book(title, author, price, pub_year))
                    case 2:
                        show_library()
                    case 3:
                        break
                    case 4:
                        book_id = int(input("\nInsert the id of the book to be removed: "))
                        remove_book(book_id)
                    case 5:
                        author_name = input("\nInsert the author name: ")
                        filter_book(author_name)
                    case 7:
                        exit(0)
        case 2:
            # Declarando variável de opção e atribuindo valor arbitrário para entrar no laço while
            option_admin = 0

            while option_admin != 4:
                print(ADMIN_MENU)
                option_admin = int(input("Insert option number: "))

                match option_admin:
                    case 1:
                        break
                    case 2:
                        import_data()
                    case 3:
                        db_backup()
                    case 5:
                        exit(0)
