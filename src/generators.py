def filter_by_currency(transactions, currency):
    """Функция принимает список словарей на вход, возвращает итератор"""
    sorted_by_currency = iter(filter(lambda x: x['operationAmount']['currency']['code'] == currency, transactions))
    return sorted_by_currency


def transaction_descriptions(transactions):
    """Функция-генератор, принимает на вход список словарей,использует yield для генерации значений по запросу."""
    for descriptions in transactions:
        yield descriptions["description"]


def card_number_generator(start, stop):
    """Функция-генератор, выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, stop):
        card_number = str(number).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
