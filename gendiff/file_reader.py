def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_format(filepath):
    if filepath.endswith('.yml') or filepath.endswith('.yaml'):
        return 'yaml'
    elif filepath.endswith('.json'):
        return 'json'
