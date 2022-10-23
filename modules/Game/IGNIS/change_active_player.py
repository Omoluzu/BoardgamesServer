"""
Смена активного игрока
"""
import jmespath


def change_active_player(current_active_player: str, users: dict) -> str:
    list_users = list(value for value in users.values())
    list_users.pop(list_users.index(current_active_player))
    return list_users[0]


"""
Omoluzu
{'F': 'Omoluzu', 'W': 'Hokage'}
"""


if __name__ == "__main__":
    assert (change_active_player(
        current_active_player="Omoluzu", users={'F': 'Omoluzu', 'W': 'Hokage'}
    )) == 'Hokage'
