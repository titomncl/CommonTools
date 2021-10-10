import os

def make_dirs(path):
    if path and not os.path.exists(path):
        os.makedirs(path)

        return True
    else:
        return False

def glob_path_recursive(path, endswith):
    for dir_path, dirs, _ in os.walk(path):
        for dir in dirs:
            file_path = os.path.join(dir_path, dir).replace("\\", "/")
            if file_path.endswith(endswith):
                return file_path
