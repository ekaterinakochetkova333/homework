import os.path


from src.utils import read_json_file


def test_read_json_file(return_read_json_file):
    read_file_json_true = read_json_file(os.path.abspath('data/operations.json'))
    read_file_json_false = read_json_file(os.path.abspath('data/operations1.json'))
    assert read_file_json_true == return_read_json_file
    assert read_file_json_false == []
