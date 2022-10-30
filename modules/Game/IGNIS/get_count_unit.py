

def get_count_unit(field) -> dict:
    f = w = 0
    for line_field in field:
        f += line_field.count('F')
        w += line_field.count('W')

    game_over = None
    match [f, w]:
        case [0, 0]:
            game_over = "draw"
        case [0, _]:
            game_over = "F"
        case [_, 0]:
            game_over = "W"

    return {"count": f"F{f}W{w}", "game_over": game_over}


if __name__ == "__main__":

    assert get_count_unit(
        field=[
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', 'E'],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ]
    ) == {"count": "F8W8", "game_over": None}

    assert get_count_unit(
        field=[
            ['F', '', '', '', 'W', 'W'],
            ['', '', '', '', '', 'W'],
            ['', '', 'F', '', '', 'E'],
            ['', '', '', 'F', '', ''],
            ['W', '', '', '', '', ''],
            ['W', 'W', '', '', '', 'F']
        ]
    ) == {"count": "F4W6", "game_over": None}

    assert get_count_unit(
        field=[
            ['', '', '', '', 'W', 'W'],
            ['', '', '', '', '', 'W'],
            ['', '', '', '', '', 'E'],
            ['', '', '', '', '', ''],
            ['W', '', '', '', '', ''],
            ['W', 'W', '', '', '', '']
        ]
    ) == {"count": "F0W6", "game_over": "F"}

    assert get_count_unit(
        field=[
            ['F', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', 'F', '', '', 'E'],
            ['', '', '', 'F', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', 'F']
        ]
    ) == {"count": "F4W0", "game_over": "W"}

    assert get_count_unit(
        field=[
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', 'E'],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ]
    ) == {"count": "F0W0", "game_over": "draw"}
