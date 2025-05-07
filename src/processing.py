from typing import Any


def filter_by_state(in_states: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрации операций по ключу state"""

    list_state = []
    for key in in_states:
        if key.get("state") == state_id:
            list_state.append(key)
    return list_state