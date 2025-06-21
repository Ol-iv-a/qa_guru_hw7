import os
from zipfile import ZipFile

import pytest

from config import ZIP_DIR, PDF_PATH, XLSX_PATH, CSV_PATH


@pytest.fixture()
def create_archive():
        with ZipFile(ZIP_DIR, 'w') as zip_file:
            zip_file.write(PDF_PATH, arcname='file.pdf')
            zip_file.write(XLSX_PATH, arcname='file.xlsx')
            zip_file.write(CSV_PATH, arcname='file.csv')

        yield

        if os.path.exists(ZIP_DIR):
            os.remove(ZIP_DIR)