from project_setup import project_setup
from constants import MAIN_MENU, LIBRARY_MENU, ADMIN_MENU
from db_tools import *
from csv_tools import *
from book import Book

project_setup()

option_main = 0
while option_main != 3:
    print(MAIN_MENU)
    option_main = int(input("Put the wished option number: "))

    match option_main:
        case 1:
            option_library = 0
            while option_library != 6:
                print(LIBRARY_MENU)
                option_library = int(input("Put the wished option number: "))

                match option_library:
                    case 1:
                        title = input("Title: ")
                        author = input("Author: ")
                        price = input("Price: ")
                        pub_year = input("Publication Year: ")

                        book = Book(title, author, price, pub_year)
                        add_book(book)
                    case 2:
                        show_library()
        case 2:
            option_admin = 0
            while option_admin != 4:
                print(ADMIN_MENU)
                option_admin = int(input("Put the wished option number: "))

                match option_admin:
                    case 1:
                        break
                    case 2:
                        import_data()
                    case 3:
                        db_backup()
