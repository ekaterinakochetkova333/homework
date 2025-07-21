import pytest

from src.decorators import my_function_no_file, my_function_yes_file


def test_log(capsys):
    my_function_no_file(5, 10)
    captured = capsys.readouterr()
    assert captured.out == "my_function_no_file ok\n"

    my_function_no_file(5, "10")
    captured = capsys.readouterr()
    assert captured.out == "my_function_no_file error: TypeError Inputs: (5, '10') {}\n"

    with open("mylog.txt", "r") as file:
        my_function_yes_file(5, 10)
        assert file.readline() == "my_function_yes_file ok"


    with open("mylog.txt", "r") as file:
        my_function_yes_file(5, "10")
        assert file.readline() == "my_function_yes_file error: TypeError Inputs: (5, '10') {}"



























# def hello_world():
#     print("Hello, world!")
# Тест с использованием
# capsys
# :
#
# def test_hello_world(capsys):
#     hello_world()
#     captured = capsys.readouterr()
#     assert captured.out == "Hello, world!\n"

# def test_greeting(capsys):
#     greeting('Earthling')
#     out, err = capsys.readouterr()
#     assert out == 'Hi, Earthling\n'
#     assert err == ''
