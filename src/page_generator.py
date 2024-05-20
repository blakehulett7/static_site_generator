import shutil
import os
from md_html import md_to_htmlnode


def extract_title(markdown_file):
    if not markdown_file.startswith("# "):
        raise Exception("Invalid markdown: Add a top level header")
    return markdown_file.split("\n")[0].lstrip("# ")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        md_file = f.read()
    with open(template_path) as f:
        template_file = f.read()
    html_file = md_to_htmlnode(md_file).to_html()
    title = extract_title(md_file)
    template_file = template_file.replace("{{ Title }}", title)
    template_file = template_file.replace("{{ Content }}", html_file)
    if os.path.exists(dest_path):
        with open(dest_path, "w") as f:
            f.write(template_file)
    else:
        with open(dest_path, "x") as f:
            f.write(template_file)
