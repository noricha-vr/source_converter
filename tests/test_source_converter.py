import os

import pytest
from pathlib import Path
from source_converter import SourceConverter


class TestSourceConverter:

    @pytest.mark.parametrize(('file_path', 'html_path'), [
        (Path("project/source_converter/source_converter/source_converter.py"),
         Path("html/source_converter/source_converter/source_converter.py.html")),
        (Path("project/source_converter/README.md"),
         Path("html/source_converter/README.html")),
    ])
    def test_file_to_html(self, file_path, html_path):
        # This test needs to run after GithubDownloader test_download_github_archive_and_unzip_to_file().
        source_converter = SourceConverter('default')
        html_file_path = source_converter.file_to_html(file_path)
        assert html_file_path.exists() is True
        assert html_file_path == html_path

    @pytest.mark.parametrize(('project_path',), [
        (Path("project/source_converter"),),
        (Path("project/UdonSharp"),),
    ])
    def test_is_binary_file(self, project_path):
        # walk through all files in the project folder
        for root, dirs, files in os.walk(project_path):
            for file in files:
                file_path = Path(root) / file
                if SourceConverter._is_binary_file(file_path): continue
                with open(file_path, 'r') as f:
                    assert f.read() is not None

    @pytest.mark.parametrize(('targets', 'count'), [
        (['*.py'], 6),
        (['*.py', 'README.md'], 7),
    ])
    def test_select_target_files(self, targets, count):
        project_folder_path = Path("project/source_converter")
        target_files = SourceConverter.select_target_files(project_folder_path, targets)
        assert len(target_files) == count

    @pytest.mark.parametrize(('project_folder', 'targets', 'count'), [
        (Path("project/source_converter"), ['README.md', '*.py'], 7),
    ])
    def test_project_to_html(self, project_folder, targets, count):
        source_converter = SourceConverter('default')
        html_paths = source_converter.project_to_html(project_folder, targets)
        assert len(html_paths) == count
