import sqlite3
from constants import BACKUPS_DIR, DB_FILEPATH
from book import Book
from datetime import date

# Inicializa o banco de dados, criando o arquivo e a tabela de livros
def db_init():
    DB_FILEPATH.touch(exist_ok=True) # Cria o arquivo do banco de dados (se necessário)

    create_table()

# Definindo a função que vai estabelecer a conexão com o banco de dados para toda e qualquer operação nele feita
def db_connection(function):
    def wrapper(*args, **kwargs):
        with sqlite3.connect(DB_FILEPATH) as conn:
            return function(conn.cursor(), *args, **kwargs)
    return wrapper


@db_connection
def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price REAL NOT NULL,   
            pub_year INTEGER NOT NULL,
            UNIQUE(title, author, pub_year)
        )
    """)


@db_connection
def no_records(cursor):
    cursor.execute("SELECT COUNT(*) FROM books")

    # Obtendo o número de registros no banco de dados
    records_num = cursor.fetchone()[0]
    return True if records_num == 0 else False


@db_connection
def add_book(cursor, book: Book):
    cursor.execute("INSERT OR IGNORE INTO books(title, author, pub_year, price) VALUES (?, ?, ?, ?)",
                   (book.title, book.author, book.pub_year, book.price))
    # Testando se o livro já não está presente no banco de dados (duplicata)
    if cursor.rowcount == 0:
        print("\nEntry error: Unable to add book. "
              "Please check if it is a duplicate or if any required information is missing.")
        return
    print("\nNew book added successfully!")


@db_connection
def show_library(cursor):
    # Montando um dicionário com os dados das tuplas retornadas usando o nome da coluna como chave
    result_dict = [{
        "id": record[0],
        "title": record[1],
        "author": record[2],
        "price": record[3],
        "pub_year": record[4]
        } for record in cursor.execute("SELECT * FROM books")
    ]
    for book in result_dict:
        print(f"""
                Id: {book["id"]}
                Title: {book["title"]}
                Author: {book["author"]}
                Price: {book["price"]}
                Publication Year: {book["pub_year"]}
        """)


@db_connection
def update_book(cursor):
    option = int(input("Enter a number according to the options: "))
    match option:
        case 3:
            return
        case 1:
            while True:
                try:
                    book_id = int(input("Insert the id to update the book price: "))
                    break
                except ValueError:
                    print("Oops, books ids must be integers.. Try again!")
                    book_id = int(input("Insert the id to update the book price: "))

            while True:
                try:
                    new_price = float(input("Insert the new price: "))
                    break
                except ValueError:
                    print("Oops, prices must be numbers.. Try again!")
                    price = float(input("Insert the new price: "))

            cursor.execute("UPDATE books SET price = ? WHERE id = ?", (new_price, book_id))

            lines_affected = cursor.rowcount
            if lines_affected == 0:
                print(f"\nError: No book with {book_id} found, please try again.")
                return
            print("\nThe price has been updated!")
        case 2:
            while True:
                try:
                    book_id = int(input("Insert the id to update the book data: "))
                    break
                except ValueError:
                    print("Oops, books ids must be integers.. Try again!")
                    book_id = int(input("Insert the id to update the book data: "))

            print("Enter the information below to update your book registration. "
                "You will be asked for the new name of the book, author, price and year of publication.")

            new_title = input("Insert the title: ")
            new_author = input("Insert the author: ")
            new_price = float(input("Insert the price: "))
            new_pub_year = int(input("Insert the year of publication: "))

            cursor.execute("""UPDATE books SET 
            title = ?,  author = ?, price = ?, pub_year = ?
            WHERE id = ?""", (new_title, new_author, new_price, new_pub_year, book_id))

            lines_affected = cursor.rowcount
            if lines_affected == 0:
                print(f"\nError: No book with {book_id} found, please try again.")
                return
            print(f"\nSuccess, book with id {book_id} information updated successfully!")
        case 4:
            exit(0)


@db_connection
def remove_book(cursor, book_id):
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))

    lines_affected = cursor.rowcount
    if lines_affected == 0:
        print(f"\nError: No book with id {book_id} found, please try again.")
        return
    print(f"\nThe book with id {book_id} information removed successfully!")


@db_connection
def filter_book(cursor, author_name: str):
    # 'COLLATE NOCASE' ignora se as letras são minúsculas ou maiúsculas
    cursor.execute("SELECT * FROM books WHERE author = ? COLLATE NOCASE", (author_name,))

    matches = cursor.fetchall()
    if len(matches) == 0:
        print(f"\nNo book written by {author_name} found")
        return

    result_dict = [{
        "id": match[0],
        "title": match[1],
        "author": match[2],
        "price": match[3],
        "pub_year": match[4]
        } for match in matches
    ]
    for book in result_dict:
        print(f"""
                Id: {book["id"]}
                Title: {book["title"]}
                Author: {book["author"]}
                Price: {book["price"]}
                Publication Year: {book["pub_year"]}
        """)


@db_connection
def db_reset(cursor):
        try:
            cursor.execute("DROP TABLE IF EXISTS books")
            create_table()
        except sqlite3.OperationalError:
            print(f"\n Verify if you have a database file called {DB_FILEPATH.name} at {DB_FILEPATH}")


def db_backup():
    # Estabelece 2 conexões, uma com o banco de dados principal e uma de "backup"
    try:
        with (sqlite3.connect(DB_FILEPATH) as conn,
                sqlite3.connect(BACKUPS_DIR / f"bk_library_{date.today()}.db") as backup_conn):
            conn.backup(backup_conn)
    except (FileNotFoundError, sqlite3.OperationalError):
        print("\nMain database or backup database not found. We suggest you to delete the 'needed dirs', "
                "rerun the program and try again.")


@db_connection
def show_statistics(cursor):
    pass
