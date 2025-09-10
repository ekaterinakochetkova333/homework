from unittest.mock import patch
from src.transactions_read import transactions_read_csv, transactions_read_excel


@patch("csv.DictReader")
def test_transactions_read_csv(mock_DictReader):
    """Тест функции для считывания финансовых операций из CSV"""
    mock_DictReader.return_value = []
    res = transactions_read_csv('data/transactions.csv')
    assert res == []

@patch("pandas.read_excel")
def test_transactions_read_excel(mock_read_excel):
    """Тест функции для считывания финансовых операций из Excel"""
    mock_read_excel.return_value.to_dict.return_value = []
    res = transactions_read_excel('data/transactions_excel.xlsx')
    assert res == []