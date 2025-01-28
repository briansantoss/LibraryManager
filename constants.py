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

ADMIN_MENU = f"""
[] - Export CSV file data
[] - Import db data to CSV format
[] - Make a database backup
[] - Reset database
[] - Generate database statistics
[] - Add a book genre
[] - Remove book genre
[] - Modify book genre
[] - Display genres
[] - Go back
[] - Exit
"""

UPDATE_MENU = """
+-------------------------------------------+
|   [1] - Update price                      |
|   [2] - Update all                        |
|   [3] - Go back                           |
|   [4] - Exit                              |
+-------------------------------------------+
"""
