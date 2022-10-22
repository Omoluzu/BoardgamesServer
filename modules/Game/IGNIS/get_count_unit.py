

def get_count_unit(field) -> str:
    f = w = 0
    for line_field in field:
        f += line_field.count('F')
        w += line_field.count('W')
    return f"F{f}W{w}"


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
    ) == "F8W8"

    assert get_count_unit(
        field=[
            ['F', '', '', '', 'W', 'W'],
            ['', '', '', '', '', 'W'],
            ['', '', 'F', '', '', 'E'],
            ['', '', '', 'F', '', ''],
            ['W', '', '', '', '', ''],
            ['W', 'W', '', '', '', 'F']
        ]
    ) == "F4W6"

