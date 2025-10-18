from src.process_bank import process_bank_search, process_bank_operations


def test_process_bank_search(transactions, bank_search):
    assert process_bank_search(transactions, 'Перевод') == bank_search


def test_process_bank_operations(transactions, bank_operations):
    assert process_bank_operations(transactions, bank_operations) == {'Перевод организации': 2,
                                                                      'Перевод с карты на карту': 1,
                                                                      'Перевод со счета на счет': 2
                                                                      }
