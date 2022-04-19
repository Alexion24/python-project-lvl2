from gendiff.data_parser import parse
from gendiff.file_reader import read_file
from gendiff.data_comparer import compare_data, stringify_diff


def generate_diff(filepath1, filepath2):
    data1 = parse(read_file(filepath1))
    data2 = parse(read_file(filepath2))
    diff = stringify_diff(compare_data(data1, data2))
    return diff
