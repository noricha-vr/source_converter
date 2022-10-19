from pathlib import Path

import pytest

from source_converter import SourceConverter


class TestSourceConverter:

    @pytest.mark.parametrize(("project_path", "copied_project_path"), [
        (Path("project/screen_capture-main"), Path("project/screen_capture-main-copy")),
    ])
    def test_copy_project(self, project_path, copied_project_path):
        assert SourceConverter.copy_project(project_path) == copied_project_path

    @pytest.mark.parametrize(('file_path', 'html_path'), [
        (Path("project/screen_capture-main_copy/main.py"), Path("project/screen_capture-main_copy/main.html")),
        (Path("project/screen_capture-main_copy/tests/test_app.py"),
         Path("project/screen_capture-main_copy/tests/test_app.html")),
    ])
    def test_file_to_html(self, file_path, html_path):
        # This test needs to run after test_copy_project
        source_converter = SourceConverter('default')
        html_file_path = source_converter.file_to_html(file_path)
        assert html_file_path.exists() is True
        assert html_file_path == html_path

    def test_project_to_html_files(self):
        project_folder_path = Path("project/screen_capture-main")
