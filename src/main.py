from static_to_public_copy import static_to_public_copy


def main():
    static_to_public_copy()
    with open("./content/index.md") as f:
        md_file = f.read()


main()
