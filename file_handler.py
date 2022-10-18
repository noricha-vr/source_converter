import hashlib
from pathlib import Path
import zipfile

import requests


class FileHandler:

    @staticmethod
    def unzip_file(zip_file_path: Path, folder_path: Path) -> None:
        """
        Unzip file
        :param zip_file_path:
        :param folder_path:
        """
        with zipfile.ZipFile(zip_file_path) as existing_zip:
            existing_zip.extractall(folder_path)

    @staticmethod
    def download_file(url: str, file_path: Path) -> None:
        """
        Download git archive
        :param url:
        :param file_path:
        """
        response = requests.get(url)
        with open(file_path, 'wb') as f:
            f.write(response.content)
