import pytest

from src.generators import card_number_generator, transaction_descriptions, filter_by_currency


@pytest.mark.parametrize("expected", [
    (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ]
    ),
    ([
        "Перевод организации",])])
def test_transaction_descriptions(transactions, for_descriptions, expected):
    """Тест, проверяющий, что функция возвращает корректные описания для каждой транзакции."""
    result_descriptions = transaction_descriptions(transactions)
    expected = for_descriptions
    assert list(result_descriptions) == expected


def test_filter_by_currency(transactions, by_currency):
    """Тест, проверяющий, что функция корректно фильтрует транзакции по заданной валюте."""
    result_currency = filter_by_currency(transactions, "USD")
    expected_result = by_currency
    assert expected_result == list(result_currency)


def test_card_number_generator():
    """Тест, проверяющий,что генератор выдает правильные номера карт в заданном диапазоне."""
    generator = card_number_generator(start=0000000000000000, stop=9999999999999999)
    assert next(generator) == "0000 0000 0000 0000"
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
