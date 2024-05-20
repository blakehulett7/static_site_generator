import os
import shutil


def main():
    print(
        directory_copy(
            "/home/smirkin_blake/workspace/github.com/blakehulett7/staticsitegenerator/static"
        )
    )


def static_to_public_copy():
    project_directory = (
        "/home/smirkin_blake/workspace/github.com/blakehulett7/staticsitegenerator"
    )
    static_directory = f"{project_directory}/static"
    public_directory = f"{project_directory}/public"
    if os.path.exists(public_directory):
        shutil.rmtree(public_directory)
    os.mkdir(public_directory)
    directory_copy(static_directory)


def directory_copy(directory_path):
    project_directory = (
        "/home/smirkin_blake/workspace/github.com/blakehulett7/staticsitegenerator"
    )
    target_directory = f"{project_directory}/public"
    directory_contents = os.listdir(directory_path)
    copied_contents = []
    for contents in directory_contents:
        path = f"{directory_path}/{contents}"
        if os.path.isfile(f"{directory_path}/{contents}"):
            shutil.copy(path, public_directory)
        else:
            copied_contents.append(directory_copy(path))
    return copied_contents


main()
