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
    directory_copy("")


def directory_copy(relative_path):
    project_directory = (
        "/home/smirkin_blake/workspace/github.com/blakehulett7/staticsitegenerator"
    )
    static_directory = f"{project_directory}/static"
    public_directory = f"{project_directory}/public"

    if relative_path == "":
        current_directory = static_directory
        target_directory = public_directory
    else:
        current_directory = static_directory + f"{relative_path}"
        target_directory = public_directory + f"{relative_path}"
        print(f"Creating public{relative_path}")
        os.mkdir(target_directory)

    directory_contents = os.listdir(current_directory)
    for content in directory_contents:
        current_path = current_directory + "/" + content
        if os.path.isfile(current_path):
            print(f"copying static/{content} into public{relative_path}")
            shutil.copy(current_path, target_directory)
        else:
            directory_copy(relative_path + "/" + f"{content}")


main()
