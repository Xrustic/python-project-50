import argparse
from .diff_builder import generate_diff


def parser():
    parser = argparse.ArgumentParser(description='Compares two configuration\n'
                                     ' files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument("-f", "--format", help='set format of output')
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)