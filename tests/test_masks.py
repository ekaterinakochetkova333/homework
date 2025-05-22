import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("number, expected_result",
                         [("1596837868705199", "1596 83** **** 5199"),
                          ("7000792289606361", "7000 79** **** 6361"),
                          ("15968378687099", "Неверный номер карты"),
                          ("700079228fkg6361", "Неверный номер карты"),
                          ("", "Неверный номер карты")])
def test_get_mask_card_number(number, expected_result):
    """Функция проверяющая правильность маскировки номера карты"""
    assert get_mask_card_number(number) == expected_result


@pytest.mark.parametrize("account, expected_result",
                         [("64686473678894779589", "**9589"),
                          ("35383033474447895560", "**5560"),
                          ("646864736788947795", "Неверный номер счета"),
                          ("35383033dh4447895560", "Неверный номер счета"),
                          ("", "Неверный номер счета")])
def test_get_mask_account(account, expected_result):
    """Функция проверяющая правильность маскировки номера счета"""
    assert get_mask_account(account) == expected_result
