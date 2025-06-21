import os

CURRENT_FILE = os.path.abspath(__file__) # получаем абсолютный путь к текущему файлу
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE  ) # получаем абсолютный путь к текущей директории, где находится файл с которым работаем
TMP_DIR = os.path.join(CURRENT_DIRECTORY, 'tmp') # делаем склейку пути к текущей директории и папки tmp
ZIP_DIR = os.path.join(TMP_DIR, "archive.zip") # делаем склейку пути к папке tmp и архива
PDF_PATH = os.path.join(TMP_DIR, "file.pdf") # делаем склейку пути к папке tmp и файлу
XLSX_PATH = os.path.join(TMP_DIR, "file.xlsx")
CSV_PATH = os.path.join(TMP_DIR, "file.csv")