import sqlite3
from constants import BACKUPS_DIR, LIBRARY_DB
from book import Book
from datetime import date


# Definindo a função que vai estabelecer a conexão com o banco de dados para toda e qualquer operação nele feita
def db_connection(function):
    def wrapper(*args, **kwargs):
        with sqlite3.connect(LIBRARY_DB) as connection:
            cursor = connection.cursor()
            return function(cursor, *args, **kwargs)
    return wrapper


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
        print("\nEntry error: Unbale to add book. "
              "Please check if it is a duplicate or if any required information is missing.")
        return
    print("\nAdded successfully")
    db_backup()


@db_connection
def show_library(cursor):
    # Realizando consulta para verificar se existe algum registro atualmente no banco de dados
    if no_records():
        print("\nThere are no books to display")
        return

    cursor.execute("SELECT * FROM books")

    query_result = cursor.fetchall()
    for record in query_result:
        print(f'''
                Id: {record[0]}
                Title: {record[1]}
                Author: {record[2]}
                Price: {record[3]}
                Publication Year: {record[4]}
                ''')


@db_connection
def update_book(cursor):
    option = int(input("Enter a number according to the options: "))

    match option:
        case 3:
            return

        case 1:
            book_id = int(input("Insert the id to update the book price: "))

            cursor.execute("SELECT COUNT(*) FROM books WHERE id = ?", (book_id,))

            # Testando se existe algum registro com o id passado via argumento
            matches_num = cursor.fetchone()[0]
            if matches_num == 0:
                print(f"\nid: {book_id} invalid, please try again")
                return

            price = float(input("Insert the new price: "))

            cursor.execute("UPDATE books SET price = ? WHERE id = ?", (price, book_id))
            print("\nThe price has been updated!")
            db_backup()

        case 2:
            book_id = int(input("Enter id to update book data: "))

            cursor.execute("SELECT COUNT(*) FROM books WHERE id = ?", (book_id,))

            # Testando se existe algum registro com o id passado via argumento
            matches_num = cursor.fetchone()[0]
            if matches_num == 0:
                print(f"\nid: {book_id} invalid, please try again")
                return

            print("Enter the information below to update your book registration. "
                "You will be asked for the new name of the book, author, price and year of publication.")

            title = input("Insert the title: ")
            author = input("Insert the author: ")
            price = float(input("Insert the price: "))
            pub_year = int(input("Insert the year of publication: "))

            cursor.execute('''UPDATE books SET 
            title = ?,  author = ?, price = ?, pub_year = ?
            WHERE id = ?''', (title, author, price, pub_year, book_id))

            print(f"\nSuccess, book with id {book_id} information updated successfully!")
            db_backup()


@db_connection
def remove_book(cursor, book_id: int):
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))

    # Verificando se houve de fato alguma remoção
    if cursor.rowcount == 0:
        print("\nBook not found")
        return
    print(f"\nBook with id {book_id} removed")
    db_backup()


@db_connection
def filter_book(cursor, author_name: str):
    # Verificando quantos livros têm o autor informado via argumento
    cursor.execute("SELECT COUNT(*) FROM books WHERE author = ?", (author_name,))

    matches_num = cursor.fetchone()[0]
    if matches_num == 0:
        print("\nNo book found")
        return

    cursor.execute("SELECT * FROM books WHERE author = ?", (author_name,))

    query_result = cursor.fetchall()
    for record_info in query_result:
        print(f'''
            Id: {record_info[0]}
            Title: {record_info[1]}
            Author: {record_info[2]}
            Price: {record_info[3]}
            Publication Year: {record_info[4]}
            ''')


def db_backup():
    # Estabelece 2 conexões, uma com o banco de dados principal e uma de backup
    with (sqlite3.connect(LIBRARY_DB) as connection,
          sqlite3.connect(BACKUPS_DIR / f"bk_library_{date.today()}.db") as backup):
        connection.backup(backup)
