import os
from pathlib import Path
from typing import List

from file_handler import FileHandler
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


class SourceConverter:
    """
    This class can do below.
    download GitHub repository.
    extract the zip file.
    convert source code to html.
    convert html to images.
    convert images to movie.
    :param css_style: You can select css_style from `default`, `emacs`, `friendly`, `colorful`.
    """

    def __init__(self, css_style='default'):
        css_dict = {
            'default': 'https://storage.googleapis.com/vrchat/css/default.css',
            'emacs': 'https://storage.googleapis.com/vrchat/css/emacs.css',
            'friendly': 'https://storage.googleapis.com/vrchat/css/friendly.css',
            'colorful': 'https://storage.googleapis.com/vrchat/css/colorful.css',
        }
        self.css_url = css_dict[css_style]

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

    def add_css(self, html: str) -> str:
        """
        Add css to html source code.
        :param html source code.
        :param css_path: css file path.
        :return: html source code with css.
        """
        return "\n".join([f'<link href="{self.css_url}" rel="stylesheet">', html])

    @staticmethod
    def add_h1(html: str, file_path: Path) -> str:
        """
        Add h1 tag to html.
        :param html:
        :param file_path:
        :return:
        """
        text = str(file_path).split('/')[1:]
        return f'<h1>{text}</h1>\n{html}'

    def file_to_html(self, file_path: Path) -> Path:
        """
        Convert file to html.
        :param file_path:
        :return html_file_path:
        """
        html_file_path = Path(str(file_path).replace('project', 'html').replace(file_path.suffix, ".html"))
        print(f"html_file_path parent: {html_file_path.parent}")
        html_file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'r') as f:
            code = f.read()
        html = highlight(code, PythonLexer(), HtmlFormatter())
        html = self.add_h1(html, file_path)
        html = self.add_css(html)
        print(html)
        with open(html_file_path, 'w') as f:
            f.write(html)
        return html_file_path

    @staticmethod
    def select_target_files(project_folder_path: Path, targets: List[str]) -> List[Path]:
        """
        Select target files from project folder. filter by target types.
        :param project_folder_path:
        :param targets:
        :return: target file paths
        """
        target_paths = []
        for target in targets:
            target_paths.extend(project_folder_path.glob(f"**/{target}"))
        return target_paths
