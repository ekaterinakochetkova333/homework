import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log', 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирующая номер карты"""

    if card_number.isdigit() and len(card_number) == 16:
        res = f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"
        logger.info(res)
        return res
    else:
        logger.warning("Неверный номер карты")
        return "Неверный номер карты"


def get_mask_account(bank_account: str) -> str:
    """Функция маскирующая номер счета"""

    if bank_account.isdigit() and len(bank_account) == 20:
        res = f"{'*' * 2}{bank_account[-4::]}"
        logger.info(res)
        return res
    else:
        logger.error("Неверный номер счета")
        return "Неверный номер счета"
