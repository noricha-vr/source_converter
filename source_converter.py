import os
from pathlib import Path
from typing import List

from file_handler import FileHandler


class SourceConverter:
    """
    This class can do below.
    download GitHub repository.
    extract the zip file.
    convert source code to html.
    convert html to images.
    convert images to movie.
    """

    @staticmethod
    def get_zip_file_path(folder_path) -> Path:
        """
        Get zip file path.
        :return: Path of zip file.
        """
        zip_file_path = Path(folder_path).parent / "master.zip"
        return zip_file_path

    @staticmethod
    def get_unzip_folder_path(zip_path) -> Path:
        """
        Get unzip folder path
        :param zip_path:
        :return: unzip folder path
        """
        return zip_path.parent.glob(f"{zip_path.stem}-*").__next__()

    @staticmethod
    def download_github_repository(url) -> Path:
        """
        Download git archive and unzip it. return the folder path.
        Download git archive
        :return: folder path
        """
        download_url = f'{url}/archive/master.zip'
        project_name = url.split('/')[-1]
        zip_file_path = Path(f"project/{project_name}.zip")
        os.makedirs(zip_file_path.parent, exist_ok=True)
        if zip_file_path.exists(): zip_file_path.unlink()
        FileHandler.download_file(download_url, zip_file_path)
        return zip_file_path

    @staticmethod
    def extract_zip_file(zip_file_path: Path) -> Path:
        """
        Unzip file
        :param zip_file_path:
        :return: unzip folder path
        """
        FileHandler.unzip_file(zip_file_path, zip_file_path.parent)
        return SourceConverter.get_unzip_folder_path(zip_file_path)

    @staticmethod
    def source_code_to_html(folder_path: Path, targets: List[str]) -> List[Path]:
        """
        Get source code files filtered by target types.
        Convert the source codes to html. Return the html file paths.
        :param folder_path: source code folder path.
        :param targets: select source code file type or name.
        :return: html file path
        """
        target_paths = []
        html_file_paths = []
        for target in targets:
            target_paths.extend(folder_path.glob(f"**/{target}"))
        for target_path in target_paths:
            html_file_path = SourceConverter.target_to_html_path(target_path)
            os.system(f"pygmentize -O full -f html -o {html_file_path} {target_path}/*")
            html_file_paths.append(html_file_path)
        return html_file_paths

    @staticmethod
    def target_to_html_path(target:Path)->Path:
        """
        Get source file path of html file path.
        /source_converter/source_converter.py -> /source_converter_html/source_converter.html
        :param target:
        :return: html file path
        """
        return Path(str(target).replace(target.suffix, ".html"))