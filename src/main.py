from static_to_public_copy import static_to_public_copy
from page_generator import generate_pages_recursive


def main():
    static_to_public_copy()
    from_path = "./content"
    template_path = "./template.html"
    dest_path = "./public"
    generate_pages_recursive(from_path, template_path, dest_path)


main()
