from gendiff.gendiff import generate_diff
from gendiff.file_reader import read_file

JSON_FILE1 = 'tests/fixtures/file1.json'
JSON_FILE2 = 'tests/fixtures/file2.json'
YAML_FILE1 = 'tests/fixtures/file1.yaml'
YAML_FILE2 = 'tests/fixtures/file2.yaml'
YML_FILE1 = 'tests/fixtures/file1.yml'
YML_FILE2 = 'tests/fixtures/file2.yml'

ANSWER_FLAT = 'tests/fixtures/answer_flat'


def get_answer(answer_path):
    return read_file(answer_path)


def test_generate_diff_json():
    assert generate_diff(JSON_FILE1, JSON_FILE2) == get_answer(ANSWER_FLAT)


def test_generate_diff_yaml():
    assert generate_diff(YML_FILE1, YML_FILE2) == get_answer(ANSWER_FLAT)
