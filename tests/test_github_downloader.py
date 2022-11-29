import pytest
from source_converter import GithubDownloader


class TestGithubDownloader:

    @pytest.mark.parametrize(('url',), [
        ('https://github.com/noricha-vr/source_converter',),
        ('https://github.com/vrchat-community/UdonSharp/',),
    ])
    def test_download_github_archive_and_unzip_to_file(self, url):
        project_name = url.split("/")[-1]
        folder_path = GithubDownloader.download_github_archive_and_unzip_to_file(url, project_name)
        project_path = GithubDownloader.rename_project(folder_path, project_name)
        assert project_path.exists() is True
