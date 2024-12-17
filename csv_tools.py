import csv
from constants import IMPORT_SAMPLEFILEPATH, IMPORTS_DIR, EXPORT_FILEPATH
from db_tools import db_connection


def generate_sample_csv():
    if not IMPORT_SAMPLEFILEPATH.exists() or IMPORT_SAMPLEFILEPATH.stat().st_size == 0:
        IMPORT_SAMPLEFILEPATH.touch()

        with open(IMPORT_SAMPLEFILEPATH, "w", encoding="utf-8", newline="") as sample_file:
            csv.writer(sample_file, delimiter=",").writerows([
                ("Title", "Author", "Price", "Pub Year"),
                ("Perigoso! Este livro contém coelhos!", "Tim Warnes", 24.90, 2024),
                ("Democracia: O Deus que falhou", "Hans-Hermann Hoppe", 86.90, 2014),
                ("É Assim que Acaba: 1", "Colleen Hoover", 38.94, 2018),
                ( "Nexus: Uma breve história das redes de informação, "
                  "da Idade da Pedra à inteligência artificial", "Yuval Noah Harari", 83.56, 2024,),
                ("A psicologia financeira: lições atemporais sobre fortuna, "
                 "ganância e felicidade", "Morgan Housel", 34.93, 2021)
            ])

@db_connection
def import_data(cursor, import_filename: str):
    try:
        # Não é necessário adicionar a extensão devido à concatenação com '.csv'
        with open(IMPORTS_DIR / (import_filename + ".csv"), "r", encoding="utf-8") as csvfile:
            next(csvfile) # Lendo a linha de cabeçalho do arquivo
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
        print(f"\nError: Please check the {import_filename} file permissions.")


@db_connection
def export_data(cursor):
    try:
        with open(EXPORT_FILEPATH, "w", newline="", encoding="utf-8") as export_file:
            # Realiza e captura as linhas da tabela correspondentes a pesquisa feita (se houverem)
            cursor.execute("SELECT * FROM books")
            query_results = cursor.fetchall()

            # Cria o leitor do arquivo CSV e escreve o resultado da consulta nele
            writer = csv.writer(export_file)
            writer.writerows(query_results)
        print(f"Successfully exported book(s).")
    except PermissionError:
        print(f"Error: Please check the {export_file.name} file permissions.")
