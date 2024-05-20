from static_to_public_copy import static_to_public_copy
from page_generator import generate_page


def main():
    static_to_public_copy()
    from_path = "./content/index.md"
    template_path = "./template.html"
    dest_path = "./public/index.html"
    generate_page(from_path, template_path, dest_path)


main()
