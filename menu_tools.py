from constants import MAIN_MENU, LIBRARY_MENU, ADMIN_MENU, UPDATE_MENU
from db_tools import add_book, db_backup, no_records, show_library, update_book, remove_book, filter_book, \
    show_statistics
from csv_tools import import_data, export_data
from book import Book

def validate_option():
    while True:
        try:
            return int(input("Insert option number: "))
        except ValueError:
            print("\nError: Please enter a integer and valid number.")


def main_menu():
    # Declarando variável de opção e atribuindo valor arbitrário para entrar no laço while
    option_main = 0

    while option_main != 3:
        print(MAIN_MENU)

        option_main = validate_option()
        match option_main:
            case 1:
                library_menu()
            case 2:
                admin_menu()


def library_menu():
    # Declarando variável de opção e atribuindo valor arbitrário para entrar no laço while
    option_library = 0
    while option_library != 6:
        print(LIBRARY_MENU)

        option_library = validate_option()
        match option_library:
            case 1:
                title = input("\nTitle: ")
                author = input("Author: ")
                price = float(input("Price: "))
                pub_year = int(input("Publication Year: "))

                add_book(Book(title, author, price, pub_year))
                db_backup()
            case 2:
                if no_records():
                    print("\nNo book(s) to display")
                else:
                    show_library()
            case 3:
                if no_records():
                    print("\nNo book to modify")
                else:
                    print(UPDATE_MENU)
                    update_book()
                    db_backup()
            case 4:
                if no_records():
                    print("\nNo book to remove")
                else:
                    book_id = int(input("\nInsert the id of the book to be removed: "))
                    remove_book(book_id)
                    db_backup()
            case 5:
                if no_records():
                    print("\nNo book to search for")
                else:
                    author_name = input("\nInsert the author name: ")
                    filter_book(author_name)
            case 7:
                exit(0)


def admin_menu():
    # Declarando variável de opção e atribuindo valor arbitrário para entrar no laço while
    option_admin = 0
    while option_admin != 5:
        print(ADMIN_MENU)

        option_admin = validate_option()
        match option_admin:
            case 1:
                if no_records():
                    print("\nNo book(s) to export.")
                else:
                    export_data()
            case 2:
                csvfile = input("\nInsert the import file name: ")
                import_data(csvfile)
            case 3:
                if no_records():
                    print("\nNo book(s) in the system. No need to backup.")
                else:
                    db_backup()
            case 4:
                if no_records():
                    print("\nThe database is empty. No data to generate and/or display statistics.")
                else:
                    show_statistics()
            case 6:
                exit(0)