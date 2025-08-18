import pytest
from src.external_api import get_transaction_amount_rub
from src.utils import read_json_file
from unittest.mock import patch
import requests

@patch("requests.request")
def test_external_api(mock_request):
    json_file = read_json_file('../data/operations.json')
    for i in json_file:
        get_transaction_amount_rub(i)
    assert mock_request.call_count == 51

@patch("requests.request")
def test_get_transaction_amount_rub(mock_request):
    in_json_file = read_json_file('../data/operations.json')
    mock_request.return_value = 31957.58
    assert get_transaction_amount_rub(in_json_file[0]) == 31957.58

