from audioop import reverse
from datetime import datetime
from operator import index

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция маскировки карты и счета"""

    check = "Счет "
    if check in card:
        new_mask = get_mask_card_number(card[len(check):])
        return check + new_mask
        # return f"{card[:5]}**{card:[-4:]}"
    else:
        reverse_str = str[::-1]
        index_space = reverse_str.find(" ")
        index_space = len(str) - index_space
        first_text = str[:index_space]
        return first_text + get_mask_account(str[index_space:])

        # return f"{card[:-12]} {card[-12:-10]}** **** {card[-4:]}"


def get_data(data: str) -> str:
    """Функция преобразования даты"""

    new_data = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    return new_data.strftime("%d.%m.%Y")
