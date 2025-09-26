import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    return [i for i in data if re.search(search, i.get("description"))]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    counts = {category: 0 for category in categories}
    for operation in data:
        desc = operation.get('description', None)
        if desc is not None and desc in categories:
            counts[desc] += 1

    return counts
