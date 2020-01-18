import os
from contextlib import contextmanager

@contextmanager
def change_dir(dst):
    try:
        cwd = os.getcwd()
        os.chdir(dst)
        yield
    finally:
        os.chdir(cwd)

with change_dir('../'):
    print(os.listdir())

with change_dir('../../'):
    print(os.listdir())