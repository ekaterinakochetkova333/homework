import requests


def get_transaction_amount_rub(transaction)-> float:
    if "operationAmount" not in transaction:
        return None
    currency_code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if currency_code == "RUB":
        return float(amount)
    elif currency_code == "USD" or currency_code == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        payload = {}
        headers = {
            "apikey": "24z0Oh9LjLrDGi9p8XyNuCwZ3k6HvEz4"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.json()
        return float(result["result"])
