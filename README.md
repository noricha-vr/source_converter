# Source Convertor

This is a project to convert the source code on GitHub into a video.

## Installation

```bash
git install git+https://github.com/noricha-vr/source_convertor.git
```

## Usage

Please see `--url` or `folder_path`.
If you want select the output movie path, please set `output` option.

```python
from github_downloader import GithubDownloader
from source_converter import SourceConverter

url = "https://github.com/noricha-vr/source_converter"
targets = ['README.md', '*.py', ]
project_name = url.split("/")[-1]
folder_path = GithubDownloader.download_github_archive_and_unzip_to_file(url, project_name)
project_path = GithubDownloader.rename_project(folder_path, project_name)
source_converter = SourceConverter('default')
target_files = SourceConverter.select_target_files(project_path, targets)
html_file_path = source_converter.file_to_html(project_path)
```

## Example

```bash
python3 github_movie_maker.py noricha-vr/source_converter
Public path/to/output.mp4
python3 github_movie_maker.py https://github.com/noricha-vr/source_converter movie.mp4
```

## Requirements

- ffmpeg
- python3
- requests
- pygments
- moviepy