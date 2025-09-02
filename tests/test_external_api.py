import os

from src.external_api import get_transaction_amount_rub
from src.utils import read_json_file
from unittest.mock import patch


@patch("requests.request")
def test_external_api(mock_request):
    json_file = read_json_file(os.path.abspath('data/operations.json'))
    for i in json_file:
        get_transaction_amount_rub(i)
    assert mock_request.call_count == 51


@patch("requests.request")
def test_get_transaction_amount_rub(mock_request):
    in_json_file = read_json_file(os.path.abspath('data/operations.json'))
    mock_request.return_value.json.return_value = [{
        "date": "2018-02-22",
        "historical": "",
        "info": {
            "rate": 148.972231,
            "timestamp": 1519328414
        },
        "query": {
            "amount": 25,
            "from": "GBP",
            "to": "JPY"
        },
        "result": 31957.58,
        "success": True
    }]
    assert get_transaction_amount_rub(in_json_file[0]) == 31957.58
