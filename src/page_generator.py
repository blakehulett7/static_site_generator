def extract_title(markdown_file):
    if not markdown_file.startswith("# "):
        raise Exception("Invalid markdown: Add a top level header")
    return markdown_file.split("\n")[0].lstrip("# ")
