import os


def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_format(filepath):
    root, ext = os.path.splitext(filepath)
    if ext == '.yml' or ext == '.yaml':
        return 'yaml'
    elif ext == '.json':
        return 'json'
