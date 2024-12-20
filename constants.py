from pathlib import Path

# Construindo o caminho completo para o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent

# Construindo o caminho completo para o resto da estrutura do projeto
BACKUPS_DIR = BASE_DIR / "backups"
DATA_DIR = BASE_DIR / "data"
EXPORTS_DIR = BASE_DIR / "exports"
IMPORTS_DIR = BASE_DIR / "imports"

NEEDED_DIRS = [
    BACKUPS_DIR,
    DATA_DIR,
    EXPORTS_DIR,
    IMPORTS_DIR
]

IMPORT_SAMPLEFILEPATH = IMPORTS_DIR / "sample.csv"

# Construindo o caminho completo para o arquivo do banco de dados
DB_FILEPATH = DATA_DIR / "library.db"
EXPORT_FILEPATH = EXPORTS_DIR / "books.csv"

# Definindo as opções/"strings" de cada um dos menus
MAIN_MENU = """
[1] - Library Options
[2] - Admin Options
[3] - Exit
"""

LIBRARY_MENU = """
[1] - Add a book
[2] - Display book(s) information(s)
[3] - Modify book
[4] - Remove a book
[5] - Filter book(s) by author
[6] - Go back
[7] - Exit
"""

ADMIN_MENU = """
[1] - Export CSV file data
[2] - Import db data to CSV format
[3] - Make a database backup
[4] - Reset database
[5] - Generate database statistics
[6] - Add a book genre
[7] - Remove book genre
[8] - Modify book genre
[9] - Go back
[10 - Exit
"""

UPDATE_MENU = """
+-------------------------------------------+
|   [1] - Update price                      |
|   [2] - Update all                        |
|   [3] - Go back                           |
|   [4] - Exit                              |
+-------------------------------------------+
"""