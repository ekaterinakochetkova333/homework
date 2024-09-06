from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(card: str) -> str:
    """Функция маскировки карты и счета"""

    if "Счет" in card:
        return f"{card[:5]}**{card:[-4:]}"
    else:
        return f"{card[:-12]} {card[-12:-10]}** **** {card[-4:]}"


def get_data(data: str) -> str:
    """Функция преобразования даты"""

    new_data = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    return new_data.strftime("%d.%m.%Y")
