from gendiff.gendiff import generate_diff
from gendiff.file_reader import read_file

ANSWER_JSON = 'tests/fixtures/answer_json'


def test_generate_diff():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    assert generate_diff(file1, file2) == read_file(ANSWER_JSON)
