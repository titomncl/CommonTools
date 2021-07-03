import os

def make_dirs(path):
    if path and not os.path.exists(path):
        os.mkdir(path)

        return True
    else:
        print("Can't create directory ", path)
        return False
