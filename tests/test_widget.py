import pytest

from src.widget import mask_account_card, get_data


@pytest.mark.parametrize("account_number, expected_result",
                         [("Счет 73654108430135874305", "Счет **4305"),
                          ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
                          ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361")])
def test_mask_account_card(account_number, expected_result):
    """Функция проверки маскировки карты и счета"""
    assert mask_account_card(account_number) == expected_result


@pytest.mark.parametrize("data, expected_result",
                         [("2024-03-11T02:26:18.671407", "11.03.2024"),
                          ("2025-10-03T02:26:18.671407", "03.10.2025")])
def test_get_data(data, expected_result):
    assert get_data(data) == expected_result
