import re
from collections import Counter

def process_bank_search(data: list[dict], search: str) -> list[dict]:
    return [i for i in data if re.search(search, i.get("description"), re.IGNORECASE)]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    counted = Counter(map(lambda x:x.get("description"), data))
    return {k:v for k, v in counted.items() if k in categories}
