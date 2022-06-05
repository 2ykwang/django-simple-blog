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
