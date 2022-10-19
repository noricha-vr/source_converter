from pathlib import Path

import pytest

from source_converter import SourceConverter


class TestSourceConverter:

    @pytest.mark.parametrize(('file_path', 'html_path'), [
        (Path("project/source_converter/main.py"), Path("html/source_converter/main.html")),
        (Path("project/source_converter/tests/test_source_converter.py"),
         Path("html/source_converter/tests/test_source_converter.html")),
    ])
    def test_file_to_html(self, file_path, html_path):
        # This test needs to run after GithubDownloader test_download_github_archive_and_unzip_to_file().
        source_converter = SourceConverter('default')
        html_file_path = source_converter.file_to_html(file_path)
        assert html_file_path.exists() is True
        assert html_file_path == html_path

    @pytest.mark.parametrize(('targets', 'count'), [
        (['*.py'], 5),
        (['*.py', 'README.md'], 6),
        (['*.py', 'README.md', ''], 6),
    ])
    def test_select_target_files(self, targets, count):
        project_folder_path = Path("project/source_converter")
        target_files = SourceConverter.select_target_files(project_folder_path, targets)
        assert len(target_files) == count
