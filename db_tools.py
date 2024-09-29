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
def add_book(cursor, book: Book):
    cursor.execute("INSERT INTO books(title, author, pub_year, price) VALUES (?, ?, ?, ?)",
                   (book.title, book.author, book.pub_year, book.price))


@db_connection
def show_library(cursor):
    # Realizando consulta para verificar quantos registros existem atualmente no banco de dados
    cursor.execute("SELECT COUNT(*) FROM books")
    records_num = cursor.fetchone()[0]
    if records_num == 0:
        print("\nThere are no books")
        return

    cursor.execute("SELECT * FROM books")

    query_result = cursor.fetchall()
    for record in query_result:
        print(f'''
                Id: {record[0]}
                Title: {record[1]},
                Author: {record[2]},
                Price: {record[3]},
                Publication Year: {record[4]}
                ''')


@db_connection
def remove_book(cursor, book_id: int):
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))

    # Verificando se houve de fato alguma remoção
    if cursor.rowcount == 0:
        print("\nBook not found")
        return
    print(f"\nBook with id {book_id} removed")


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
          sqlite3.connect(BACKUPS_DIR / f"db_library-{date.today()}.db") as backup):
        connection.backup(backup)
