import os
import shutil


def main():
    static_to_public_copy()


def static_to_public_copy():
    project_directory = (
        "/home/smirkin_blake/workspace/github.com/blakehulett7/staticsitegenerator"
    )
    static_directory = f"{project_directory}/static"
    public_directory = f"{project_directory}/public"
    if os.path.exists(public_directory):
        shutil.rmtree(public_directory)
    os.mkdir(public_directory)


main()
