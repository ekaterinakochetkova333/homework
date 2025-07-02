from src.generators import card_number_generator, transaction_descriptions, filter_by_currency


def test_transaction_descriptions(transactions, for_descriptions):
    result_descriptions = transaction_descriptions(transactions)
    ex_result = for_descriptions
    assert ex_result == list(result_descriptions)


def test_filter_by_currency(transactions, by_currency):
    result_currency = filter_by_currency(transactions, "USD")
    expected_result = by_currency
    assert expected_result == list(result_currency)


def test_card_number_generator():
    generator = card_number_generator(start= 0000000000000000, stop= 9999999999999999)
    assert next(generator) == "0000 0000 0000 0000"
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"