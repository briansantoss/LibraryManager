import sqlite3
from constants import BACKUPS_DIR, LIBRARY_DB
from datetime import date


# Definindo a função que vai estabelecer a conexão com o banco de dados para toda e qualquer operação nele feita
def db_connection(function):
    def wrapper(*args, **kwargs):
        with sqlite3.connect(LIBRARY_DB) as connection:
            cursor = connection.cursor()
            function(cursor, *args, **kwargs)
    return wrapper


@db_connection
def add_book(cursor, book):
    cursor.execute("INSERT INTO books(title, author, pub_year, price) VALUES (?, ?, ?, ?)",
                   (book.title, book.author, book.pub_year, book.price))


@db_connection
def show_library(cursor):
    cursor.execute("SELECT * FROM books")

    if cursor.rowcount == 0:
        print("No books found.")
        return

    query_result = cursor.fetchall()
    for row in query_result:
        print(f'''
        Id: {row[0]}
        Title: {row[1]},
        Author: {row[2]},
        Price: {row[3]}
        Publication Year: {row[4]},
        ''')


@db_connection
def remove_book(cursor, book_id):
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))


def db_backup():
    with (sqlite3.connect(LIBRARY_DB) as connection,
          sqlite3.connect(BACKUPS_DIR / f"db_library-{date.today()}.db") as backup):
        connection.backup(backup)
