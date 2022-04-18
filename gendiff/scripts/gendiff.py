import argparse


def main():
    parser = argparse.ArgumentParser(
        usage='gendiff [-h] [-f FORMAT] first_file second_file',
        description='Generate diff',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f FORMAT', '--format FORMAT', action='store_true',
                        help='set format of output')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
