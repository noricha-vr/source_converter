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
from source_converter import SourceConverter

source_converter = SourceConverter()
folder_path = source_converter.download_github_source(url="")
html_root_path = source_converter.to_html(folder_path=folder_path)
image_paths = source_converter.to_images(html_root_path=html_root_path)
movie_path = source_converter.to_movie(image_paths=image_paths)
```

## Example

```bash
python3 github_movie_maker.py noricha-vr/screen_capture path/to/output.mp4
python3 github_movie_maker.py https://github.com/noricha-vr/source_converter movie.mp4
```

## Requirements

- ffmpeg
- python3
- requests
- pygments
- moviepy