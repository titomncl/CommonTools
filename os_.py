import os

def make_dirs(path):
    if path and not os.path.exists(path):
        os.makedirs(path)

        return True
    else:
        return False
