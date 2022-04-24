from gendiff.gendiff import generate_diff
from gendiff.file_reader import read_file

JSON_FILE1 = 'tests/fixtures/file1.json'
JSON_FILE2 = 'tests/fixtures/file2.json'
YAML_FILE1 = 'tests/fixtures/file1.yaml'
YAML_FILE2 = 'tests/fixtures/file2.yaml'
YML_FILE1 = 'tests/fixtures/file1.yml'
YML_FILE2 = 'tests/fixtures/file2.yml'
NESTED_JSON_FILE1 = 'tests/fixtures/file1_nested.json'
NESTED_JSON_FILE2 = 'tests/fixtures/file2_nested.json'
NESTED_YAML_FILE1 = 'tests/fixtures/file1_nested.yaml'
NESTED_YAML_FILE2 = 'tests/fixtures/file2_nested.yaml'

ANSWER_STYLISH_FLAT = 'tests/fixtures/answer_stylish_flat'
ANSWER_STYLISH_NESTED = 'tests/fixtures/answer_stylish_nested'


def get_answer(answer_path):
    return read_file(answer_path)


def test_generate_diff_json():
    assert generate_diff(JSON_FILE1, JSON_FILE2)\
           == get_answer(ANSWER_STYLISH_FLAT)


def test_generate_diff_yaml():
    assert generate_diff(YML_FILE1, YML_FILE2)\
           == get_answer(ANSWER_STYLISH_FLAT)


def test_generate_diff_nested():
    assert generate_diff(NESTED_JSON_FILE1, NESTED_JSON_FILE2) \
           == get_answer(ANSWER_STYLISH_NESTED)
    assert generate_diff(NESTED_YAML_FILE1, NESTED_YAML_FILE2) \
           == get_answer(ANSWER_STYLISH_NESTED)
