import csv
from db_tools import db_connection
from project_setup import EXPORTS_DIR, IMPORTS_DIR

# Definindo o nome do arquivo de exportação
IMPORT_FILENAME = "books.csv"


@db_connection
def export_data(cursor, export_filename: str):
    try:
        with open(EXPORTS_DIR / (export_filename + ".csv"), "r", encoding="utf-8") as csvfile:
            file_rows = csv.reader(csvfile)
            cursor.executemany("INSERT INTO books(title, author, price, pub_year) VALUES (?, ?, ?, ?)", file_rows)
    except FileNotFoundError:
        print(f"Error:\nNo file named {export_filename} found at exports dir")


@db_connection
def import_data(cursor):
    with open(IMPORTS_DIR / IMPORT_FILENAME, "w", newline="", encoding="utf-8") as export_file:
        # Realiza e captura os registros da tabela correspondentes a pesquisa feita (se houverem)
        cursor.execute("SELECT * FROM books")
        query_results = cursor.fetchall()

        # Cria o leitor do arquivo CSV e escreve o resultado da consulta nele
        writer = csv.writer(export_file)
        writer.writerows(query_results)
