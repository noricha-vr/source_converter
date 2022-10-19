from pathlib import Path

import pytest

from source_converter import SourceConverter


class TestSourceConverter:

    @pytest.mark.parametrize(('file_path', 'html_path'), [
        (Path("project/screen_capture-main_copy/main.py"), Path("html/screen_capture-main_copy/main.html")),
        (Path("project/screen_capture-main_copy/tests/test_app.py"),
         Path("html/screen_capture-main_copy/tests/test_app.html")),
    ])
    def test_file_to_html(self, file_path, html_path):
        # This test needs to run after GithubDownloader test_download_github_archive_and_unzip_to_file().
        source_converter = SourceConverter('default')
        html_file_path = source_converter.file_to_html(file_path)
        assert html_file_path.exists() is True
        assert html_file_path == html_path

    @pytest.mark.parametrize(('targets', 'count'), [
        (['*.py'], 14),
        (['*.py', 'README.md'], 15),
    ])
    def test_select_target_files(self, targets, count):
        project_folder_path = Path("project/screen_capture-main_copy")
        target_files = SourceConverter.select_target_files(project_folder_path, targets)
        assert len(target_files) == count
