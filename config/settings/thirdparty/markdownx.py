# https://python-markdown.github.io/reference/#extensions

MARKDOWNX_MARKDOWN_EXTENSIONS = [
    "markdown.extensions.codehilite",
    "markdown.extensions.fenced_code",
    "markdown.extensions.extra",
    "markdown.extensions.toc",
]

MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS = {
    "markdown.extensions.codehilite": {
        "linenums": True,
        "use_pygments": True,
        "noclasses": True,
    }
}
MARKDOWNX_IMAGE_MAX_SIZE = {
    "size": (2000, 0),
    "quality": 100,
}
MARKDOWNX_MEDIA_PATH = "uploads/"
MARKDOWNX_URLS_PATH = "/editor/markdownify/"
MARKDOWNX_UPLOAD_URLS_PATH = "/editor/upload/"
