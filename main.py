from src.widget import mask_account_card

list_account = []
list_account.append("Visa Platinum 7000792289606361")
list_account.append("Maestro 7000792289606361")
list_account.append("Счет 73654108430135874305")


for acc in list_account:
    res = mask_account_card(acc)
    print(res)
