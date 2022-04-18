import argparse

parser = argparse.ArgumentParser(
    usage='gendiff [-h] first_file second_file',
    description='Generate diff',
)
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()
print(args)
