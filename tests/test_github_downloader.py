from pathlib import Path

from github_downloader import GithubDownloader


def test_download_github_archive_and_unzip_to_file():
    url = "https://github.com/noricha-vr/screen_capture"
    file_path = Path("project/screen_capture.zip")
    folder_path = GithubDownloader.download_github_archive_and_unzip_to_file(url, file_path)
    assert file_path.exists() is True
    assert folder_path.exists() is True
