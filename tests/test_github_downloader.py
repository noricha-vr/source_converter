from pathlib import Path

from github_downloader import GithubDownloader


def test_download_github_archive_and_unzip_to_file():
    url = "https://github.com/noricha-vr/source_converter"
    project_name = url.split("/")[-1]
    file_path = Path(f"project/{project_name}.zip")
    folder_path = GithubDownloader.download_github_archive_and_unzip_to_file(url, file_path)
    assert file_path.exists() is True
    project_path = GithubDownloader.rename_project(folder_path, url.split('/')[-1])
    assert project_path.exists() is True
