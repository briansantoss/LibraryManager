from db_tools import add_book, db_backup, has_books, show_library, update_book, remove_book, filter_book, \
    show_statistics, db_reset, add_genre, remove_genre
from csv_tools import import_data, export_data
from book import Book
from enum import IntEnum, auto


class LibOpt(IntEnum):
    ADD_BOOK = auto(),
    DISPLAY_BOOKS = auto(),
    MODIFY_BOOK = auto(),
    REMOVE_BOOK = auto()
    FILTER_BOOK = auto(),
    GO_BACK = auto(),
    EXIT = auto()


class AdmOpt(IntEnum):
    EXPORT_CSV_FILE_DATA = auto(),
    IMPORT_TO_CSV_FORMAT = auto(),
    MAKE_BACKUP = auto(),
    RESET_DATABASE = auto(),
    ADD_GENRE = auto(),
    DISPLAY_GENRE = auto(),
    MODIFY_GENRE = auto(),
    REMOVE_GENRE = auto(),
    GO_BACK = auto(),
    EXIT = auto()


def validate_option():
    while True:
        try:
            return int(input("Insert option number: "))
        except ValueError:
            print("\nError: Please enter a integer and valid number.")

def main_menu():
    MAIN_MENU = """
    [1] - Library options
    [2] - Admin options
    [3] - Exit
    """
    # Declarando variável de opção e atribuindo valor arbitrário para entrar no laço while
    main_opt = 0

    while main_opt:
        print(MAIN_MENU)

        main_opt = validate_option()
        match main_opt:
            case 1:
                library_menu()
            case 2:
                admin_menu()


def library_menu():
    # Declarando variável que armazena a string do menu da biblioteca
    LIBRARY_MENU = "\n".join([f"[{opt}] - {opt.name.capitalize().replace("_", " ")}" for opt in LibOpt])

    lib_opt = 0
    while lib_opt != LibOpt.GO_BACK:
        print(LIBRARY_MENU)

        lib_opt = validate_option()
        match lib_opt:
            case LibOpt.ADD_BOOK:
                title = input("\nTitle: ")
                author = input("Author: ")
                price = float(input("Price: "))
                pub_year = int(input("Publication Year: "))

                add_book(Book(title, author, price, pub_year))
                db_backup()
            case LibOpt.DISPLAY_BOOKS:
                if has_books():
                    print("\nNo book(s) to display")
                else:
                    show_library()
            case LibOpt.MODIFY_BOOK:
                if has_books():
                    print("\nNo book to modify")
                else:
                    print(UPDATE_MENU)
                    update_book()
                    db_backup()
            case LibOpt.REMOVE_BOOK:
                if has_books():
                    print("\nNo book to remove")
                else:
                    book_id = int(input("\nInsert the id of the book to be removed: "))
                    remove_book(book_id)
                    db_backup()
            case LibOpt.FILTER_BOOK:
                if has_books():
                    print("\nNo book to search for")
                else:
                    author_name = input("\nInsert the author name: ")
                    filter_book(author_name)
            case LibOpt.EXIT:
                exit(0)


def admin_menu():
    # Declarando variável que armazena a string do menu de funções administrativas
    ADMIN_MENU = "\n".join([f"[{opt}] - {opt.name.capitalize().replace("_", " ")}" for opt in AdmOpt])

    adm_opt = 0
    while adm_opt != AdmOpt.GO_BACK:
        print(ADMIN_MENU)

        adm_opt = validate_option()
        match adm_opt:
            case AdmOpt.EXPORT_CSV_FILE_DATA:
                if has_books():
                    print("\nNo book(s) to export.")
                else:
                    export_data()
            case AdmOpt.IMPORT_TO_CSV_FORMAT:
                csvfile = input("\nInsert the import file name: ")
                import_data(csvfile)
            case AdmOpt.MAKE_BACKUP:
                if has_books():
                    print("\nNo book(s) in the system. No need to backup.")
                else:
                    db_backup()
            case AdmOpt.RESET_DATABASE:
                if has_books():
                    print("\nNo book(s) in the system. No need to reset.")
                else:
                    db_reset()
            case AdmOpt.ADD_GENRE:
                genre_name = input("\nInsert the genre name: ")
                add_genre(genre_name)
            case AdmOpt.REMOVE_GENRE:
                genre_id = int(input("\nInsert the id of the genre to be removed: "))
                remove_genre(genre_id)
            case AdmOpt.EXIT:
                exit(0)
