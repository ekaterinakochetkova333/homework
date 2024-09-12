from typing import Any


def filter_by_state(in_states: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрации операций по ключу state"""

    list_state = []
    for key in in_states:
        if key.get("state") == state_id:
            list_state.append(key)
    return list_state


def sort_by_date(in_states: list[dict[str, Any]], reverse_list: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки операций по дате"""

    sorted_in_state = sorted(in_states, key=lambda in_states: in_states["date"], reverse=reverse_list)
    return sorted_in_state
