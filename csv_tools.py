import csv
from db_tools import db_connection, db_backup
from project_setup import EXPORTS_DIR, EXPORT_FILEPATH, IMPORTS_DIR


@db_connection
def import_data(cursor, import_filename: str):
    try:
        with open(IMPORTS_DIR / (import_filename + ".csv"), "r", encoding="utf-8") as csvfile:
            file_rows = csv.reader(csvfile)

            valid_rows = list(filter(lambda row: len(row) == 4, file_rows))
            if len(valid_rows) == 0:
                print(f"Error: {import_filename} file is not according to the expected format.")
                return
            
            cursor.executemany("""INSERT OR IGNORE INTO books(title, author, price, pub_year) 
            VALUES (?, ?, ?, ?)""", valid_rows)

            imported_books = cursor.rowcount 
            if imported_books == 0:
                print("\nEntry error: Unbale to add book(s).",
                      "Please check if it have duplicates or if any required information is missing.")
                return
            print(f"\nSuccessfully imported {imported_books} book(s).")
    except FileNotFoundError:
        print(f"\nError: No file named {import_filename} found at exports dir ('{IMPORTS_DIR}')")
    except PermissionError:
        print(f"Error: Please check the {import_filename} file permissions.")


@db_connection
def export_data(cursor):
    try:
        with open(EXPORT_FILEPATH, "w", newline="", encoding="utf-8") as export_file:
            # Realiza e captura os registros da tabela correspondentes a pesquisa feita (se houverem)
            cursor.execute("SELECT * FROM books")
            query_results = cursor.fetchall()

            # Cria o leitor do arquivo CSV e escreve o resultado da consulta nele
            writer = csv.writer(export_file)
            writer.writerows(query_results)
        print(f"Successfully exported book(s).")
    except PermissionError:
        print(f"Error: Please check the {export_file.name} file permissions.")
