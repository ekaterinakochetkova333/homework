from src.decorators import my_function_no_file, my_function_yes_file


def test_log(capsys):
    my_function_no_file(5, 10)
    captured = capsys.readouterr()
    assert captured.out == "my_function_no_file ok\n"

    my_function_no_file(5, "10")
    captured = capsys.readouterr()
    assert captured.out == "my_function_no_file error: TypeError Inputs: (5, '10') {}\n"
    with open("mylog.txt", "w"):
        pass
    with open("mylog.txt", "r") as file:
        my_function_yes_file(5, 10)
        my_function_yes_file(5, "10")
        lines = file.readlines()
        assert lines[0] == "my_function_yes_file ok\n"
        assert lines[1] == "my_function_yes_file error: TypeError Inputs: (5, '10') {}\n"
