import shutil
import os
import pathlib
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


def generate_pages_recursive(src_dir_path, template_path, dest_dir_path):
    src_dir_list = os.listdir(src_dir_path)
    for file in src_dir_list:
        extension = pathlib.PurePath(file).suffix
        current_path = src_dir_path + "/" + file
        if extension == ".md":
            html_file = file.strip(extension) + ".html"
            dest_path = dest_dir_path + "/" + html_file
            generate_page(current_path, template_path, dest_path)
        elif not os.path.isfile(current_path):
            new_dest_dir_path = dest_dir_path + "/" + file
            os.mkdir(new_dest_dir_path)
            generate_pages_recursive(current_path, template_path, new_dest_dir_path)


"""
content_dir = "./content"
template = "./template.html"
public_dir = "./public"
generate_pages_recursive(content_dir, template, public_dir)
"""
