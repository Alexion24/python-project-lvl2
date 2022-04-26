import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        usage='gendiff [-h] [-f FORMAT] first_file second_file',
        description='Generate diff'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        choices=['stylish', 'plain'],
        help='set format of output (stylish by default)'
    )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
