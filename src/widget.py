
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция маскировки карты и счета"""

    check = "Счет "
    if check in card:
        new_mask = get_mask_account(card[len(check):])
        return check + new_mask

    else:
        reverse_str = card[::-1]
        index_space = reverse_str.find(" ")
        index_space = len(card) - index_space
        first_text = card[:index_space]
        return first_text + get_mask_card_number(card[index_space:])


def get_data(data: str) -> str:
    """Функция преобразования даты"""

    new_data = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    return new_data.strftime("%d.%m.%Y")
