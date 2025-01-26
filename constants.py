from itertools import count
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

opt_ind = count(start=1)
# Definindo as opções/"strings" de cada um dos menus
MAIN_MENU = f"""
[{next(opt_ind)}] - Library Options
[{next(opt_ind)}] - Admin Options
[{next(opt_ind)}] - Exit
"""

opt_ind = count(start=1)
LIBRARY_MENU = f"""
[{next(opt_ind)}] - Add a book
[{next(opt_ind)}] - Display book(s) information(s)
[{next(opt_ind)}] - Modify book
[{next(opt_ind)}] - Remove a book
[{next(opt_ind)}] - Filter book(s) by author
[{next(opt_ind)}] - Go back
[{next(opt_ind)}] - Exit
"""

opt_ind = count(start=1)
ADMIN_MENU = f"""
[{next(opt_ind)}] - Export CSV file data
[{next(opt_ind)}] - Import db data to CSV format
[{next(opt_ind)}] - Make a database backup
[{next(opt_ind)}] - Reset database
[{next(opt_ind)}] - Generate database statistics
[{next(opt_ind)}] - Add a book genre
[{next(opt_ind)}] - Remove book genre
[{next(opt_ind)}] - Modify book genre
[{next(opt_ind)}] - Display genres
[{next(opt_ind)}] - Go back
[{next(opt_ind)}] - Exit
"""

UPDATE_MENU = """
+-------------------------------------------+
|   [1] - Update price                      |
|   [2] - Update all                        |
|   [3] - Go back                           |
|   [4] - Exit                              |
+-------------------------------------------+
"""
