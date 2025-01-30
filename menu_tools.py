from db_tools import add_book, db_backup, has_books, has_genres, print_genres, show_library, update_book, remove_book, filter_book, db_reset, add_genre, remove_genre
from csv_tools import import_data, export_data
from book import Book
from enum import IntEnum, auto


class MainOpt(IntEnum):
    LIBRARY_OPTIONS = auto(),
    ADMIN_OPTIONS = auto(),
    EXIT = auto()


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
    DISPLAY_GENRES = auto(),
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


def generate_menu(IntEnum):
    return  f"\n{"\n".join([f"[{opt:2}] - {opt.name.replace("_", " ").capitalize()}" for opt in IntEnum])}\n"


def main_menu():
    # Declarando variável que armazena a string do menu principal
    main_menu = generate_menu(MainOpt)

    # Declarando variável de opção e atribuindo valor arbitrário para entrar no laço while
    main_opt = 0
    while main_opt != MainOpt.EXIT:
        print(main_menu)

        main_opt = validate_option()
        match main_opt:
            case MainOpt.LIBRARY_OPTIONS:
                library_menu()
            case MainOpt.ADMIN_OPTIONS:
                admin_menu()


def library_menu():
    # Declarando variável que armazena a string do menu da biblioteca
    lib_menu = generate_menu(LibOpt)

    lib_opt = 0
    while lib_opt != LibOpt.GO_BACK:
        print(lib_menu)

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
    adm_menu = generate_menu(AdmOpt)

    adm_opt = 0
    while adm_opt != AdmOpt.GO_BACK:
        print(adm_menu)

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
            case AdmOpt.DISPLAY_GENRES:
                if has_genres():
                    print_genres()
                else:
                    print(f"\nNo genres in the system.")
            case AdmOpt.REMOVE_GENRE:
                genre_id = int(input("\nInsert the id of the genre to be removed: "))
                remove_genre(genre_id)
            case AdmOpt.EXIT:
                exit(0)
