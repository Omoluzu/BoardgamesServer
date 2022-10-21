"""

Выставление юнита на поле

"""


def expose_unit(field, route, position, tile, *args, **kwargs) -> dict:
    save_tile = {'earth': 'E', 'air': 'A'}[tile]
    tile = []

    current_move = {'tile': save_tile, 'old_pos': None}
    for i in range(5, -1, -1) if route in ['left', 'up'] else range(6):
        current_tile = ''
        x = position if route in ['left', 'right'] else i
        y = i if route in ['left', 'right'] else position

        if field[x][y] != 'X':
            if field[x][y]:
                current_tile = field[x][y]

            if save_tile:
                current_move['new_pos'] = [x, y]
                tile.append(current_move)
                field[x][y], save_tile = save_tile, current_tile
                current_move = {'tile': save_tile, 'old_pos': [x, y]}
    else:
        if save_tile:
            tile.append({'tile': save_tile, 'old_pos': tile[-1]['new_pos'], 'new_pos': 'X'})

    return {"field": field, 'move': tile}


if __name__ == '__main__':
    import copy

    data = [
        ['F', 'F', '', '', 'W', 'W'],
        ['F', '', '', '', '', 'W'],
        ['', '', 'F', 'W', '', ''],
        ['', '', 'W', 'F', '', ''],
        ['W', '', '', '', '', 'F'],
        ['W', 'W', '', '', 'F', 'F']
    ]
    data_x_button = [
        ['X', 'X', 'X', 'X', 'X', 'X'],
        ['F', 'F', '', '', 'W', 'W'],
        ['F', '', 'F', 'W', '', 'W'],
        ['', '', 'W', 'F', '', 'E'],
        ['W', '', '', '', '', 'F'],
        ['W', 'W', '', '', 'F', 'F']
    ]
    data_x_up = [
        ['F', 'F', '', '', 'W', 'W'],
        ['F', '', '', '', '', 'W'],
        ['', '', 'F', 'W', '', ''],
        ['', '', 'W', 'F', '', 'F'],
        ['W', '', '', '', 'F', 'F'],
        ['X', 'X', 'X', 'X', 'X', 'X']
    ]
    data_x_left = [
            ['F', 'F', '', 'W', 'W', 'X'],
            ['F', '', '', '', 'W', 'X'],
            ['', '', 'F', 'W', '', 'X'],
            ['', '', 'W', 'F', '', 'X'],
            ['W', '', '', '', '', 'X'],
            ['W', 'W', '', '', 'F', 'X']
        ]
    data_x_right = [
        ['X', 'F', 'F', '', 'W', 'W'],
        ['X', 'F', '', '', '', 'W'],
        ['X', '', 'F', 'W', '', ''],
        ['X', '', 'W', 'F', '', ''],
        ['X', '', '', '', '', 'F'],
        ['X', 'W', '', '', 'F', 'F']
    ]
    data_full = [
        ['F', 'F', 'E', 'E', 'W', 'W'],
        ['F', '', '', '', '', 'W'],
        ['', '', 'F', 'W', '', ''],
        ['', '', 'W', 'F', '', ''],
        ['W', '', '', '', '', 'F'],
        ['W', 'W', '', '', 'F', 'F']
    ]
    data_full_2 = [
        ['X', 'F', 'E', 'E', 'W', 'W'],
        ['X', '', '', '', '', 'W'],
        ['X', '', 'F', 'W', '', ''],
        ['X', '', 'W', 'F', '', ''],
        ['X', '', '', '', '', 'F'],
        ['X', 'W', '', '', 'F', 'F']
    ]

    assert expose_unit(copy.deepcopy(data), 'left', 0, 'earth') == {
        "field": [
            ['F', 'F', '', 'W', 'W', 'E'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        "move": [
            {'tile': 'E', 'old_pos': None, 'new_pos': [0, 5]},
            {'tile': 'W', 'old_pos': [0, 5], 'new_pos': [0, 4]},
            {'tile': 'W', 'old_pos': [0, 4], 'new_pos': [0, 3]}
        ]
    }
    assert expose_unit(copy.deepcopy(data_full), 'left', 0, 'earth') == {
        "field": [
            ['F', 'E', 'E', 'W', 'W', 'E'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        "move": [
            {'new_pos': [0, 5], 'old_pos': None, 'tile': 'E'},
            {'new_pos': [0, 4], 'old_pos': [0, 5], 'tile': 'W'},
            {'new_pos': [0, 3], 'old_pos': [0, 4], 'tile': 'W'},
            {'new_pos': [0, 2], 'old_pos': [0, 3], 'tile': 'E'},
            {'new_pos': [0, 1], 'old_pos': [0, 2], 'tile': 'E'},
            {'new_pos': [0, 0], 'old_pos': [0, 1], 'tile': 'F'},
            {'new_pos': 'X', 'old_pos': [0, 0], 'tile': 'F'}
        ]
    }
    assert expose_unit(copy.deepcopy(data_full_2), 'left', 0, 'earth') == {
        "field": [
            ['X', 'E', 'E', 'W', 'W', 'E'],
            ['X', '', '', '', '', 'W'],
            ['X', '', 'F', 'W', '', ''],
            ['X', '', 'W', 'F', '', ''],
            ['X', '', '', '', '', 'F'],
            ['X', 'W', '', '', 'F', 'F']
        ],
        "move": [
            {'new_pos': [0, 5], 'old_pos': None, 'tile': 'E'},
            {'new_pos': [0, 4], 'old_pos': [0, 5], 'tile': 'W'},
            {'new_pos': [0, 3], 'old_pos': [0, 4], 'tile': 'W'},
            {'new_pos': [0, 2], 'old_pos': [0, 3], 'tile': 'E'},
            {'new_pos': [0, 1], 'old_pos': [0, 2], 'tile': 'E'},
            {'new_pos': 'X', 'old_pos': [0, 1], 'tile': 'F'}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'left', 1, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', 'W', 'E'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [1, 5]},
            {'tile': 'W', 'old_pos': [1, 5], 'new_pos': [1, 4]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'left', 2, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', 'E'],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [2, 5]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'left', 3, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', 'E'],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [3, 5]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'left', 4, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', 'F', 'E'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [4, 5]},
            {'tile': 'F', 'old_pos': [4, 5], 'new_pos': [4, 4]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'left', 5, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', 'F', 'F', 'E']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [5, 5]},
            {'tile': 'F', 'old_pos': [5, 5], 'new_pos': [5, 4]},
            {'tile': 'F', 'old_pos': [5, 4], 'new_pos': [5, 3]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'left', 0, 'air') == {
        "field": [
            ['F', 'F', '', 'W', 'W', 'A'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [0, 5]},
            {'tile': 'W', 'old_pos': [0, 5], 'new_pos': [0, 4]},
            {'tile': 'W', 'old_pos': [0, 4], 'new_pos': [0, 3]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'left', 1, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', 'W', 'A'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [1, 5]},
            {'tile': 'W', 'old_pos': [1, 5], 'new_pos': [1, 4]}
        ]
    }
    assert expose_unit(copy.deepcopy(data_x_left), 'left', 1, 'air') == {
        "field": [
            ['F', 'F', '', 'W', 'W', 'X'],
            ['F', '', '', 'W', 'A', 'X'],
            ['', '', 'F', 'W', '', 'X'],
            ['', '', 'W', 'F', '', 'X'],
            ['W', '', '', '', '', 'X'],
            ['W', 'W', '', '', 'F', 'X']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [1, 4]},
            {'tile': 'W', 'old_pos': [1, 4], 'new_pos': [1, 3]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'left', 2, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', 'A'],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [2, 5]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'left', 3, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', 'A'],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ], 'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [3, 5]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'left', 4, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', 'F', 'A'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [4, 5]},
            {'tile': 'F', 'old_pos': [4, 5], 'new_pos': [4, 4]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'left', 5, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', 'F', 'F', 'A']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [5, 5]},
            {'tile': 'F', 'old_pos': [5, 5], 'new_pos': [5, 4]},
            {'tile': 'F', 'old_pos': [5, 4], 'new_pos': [5, 3]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'right', 0, 'earth') == {
        "field": [
            ['E', 'F', 'F', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [0, 0]},
            {'tile': 'F', 'old_pos': [0, 0], 'new_pos': [0, 1]},
            {'tile': 'F', 'old_pos': [0, 1], 'new_pos': [0, 2]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'right', 1, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['E', 'F', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [1, 0]},
            {'tile': 'F', 'old_pos': [1, 0], 'new_pos': [1, 1]}
        ]
    }
    assert expose_unit(copy.deepcopy(data_x_right), 'right', 1, 'earth') == {
        "field": [
            ['X', 'F', 'F', '', 'W', 'W'],
            ['X', 'E', 'F', '', '', 'W'],
            ['X', '', 'F', 'W', '', ''],
            ['X', '', 'W', 'F', '', ''],
            ['X', '', '', '', '', 'F'],
            ['X', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [1, 1]},
            {'tile': 'F', 'old_pos': [1, 1], 'new_pos': [1, 2]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'right', 2, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['E', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ], 'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [2, 0]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'right', 3, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['E', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [3, 0]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'right', 4, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['E', 'W', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [4, 0]},
            {'tile': 'W', 'old_pos': [4, 0], 'new_pos': [4, 1]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'right', 5, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['E', 'W', 'W', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [5, 0]},
            {'tile': 'W', 'old_pos': [5, 0], 'new_pos': [5, 1]},
            {'tile': 'W', 'old_pos': [5, 1], 'new_pos': [5, 2]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'right', 0, 'air') == {
        "field": [
            ['A', 'F', 'F', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [0, 0]},
            {'tile': 'F', 'old_pos': [0, 0], 'new_pos': [0, 1]},
            {'tile': 'F', 'old_pos': [0, 1], 'new_pos': [0, 2]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'right', 1, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['A', 'F', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [1, 0]},
            {'tile': 'F', 'old_pos': [1, 0], 'new_pos': [1, 1]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'right', 2, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['A', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [2, 0]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'right', 3, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['A', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [3, 0]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'right', 4, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['A', 'W', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [4, 0]},
            {'tile': 'W', 'old_pos': [4, 0], 'new_pos': [4, 1]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'right', 5, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['A', 'W', 'W', '', 'F', 'F']
        ], 'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [5, 0]},
            {'tile': 'W', 'old_pos': [5, 0], 'new_pos': [5, 1]},
            {'tile': 'W', 'old_pos': [5, 1], 'new_pos': [5, 2]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'up', 0, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['W', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['E', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [5, 0]},
            {'tile': 'W', 'old_pos': [5, 0], 'new_pos': [4, 0]},
            {'tile': 'W', 'old_pos': [4, 0], 'new_pos': [3, 0]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'up', 1, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', 'W', '', '', '', 'F'],
            ['W', 'E', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [5, 1]},
            {'tile': 'W', 'old_pos': [5, 1], 'new_pos': [4, 1]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'up', 2, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', 'E', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [5, 2]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'up', 3, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', 'E', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [5, 3]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'up', 4, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', 'F', 'F'],
            ['W', 'W', '', '', 'E', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [5, 4]},
            {'tile': 'F', 'old_pos': [5, 4], 'new_pos': [4, 4]}
        ]
    }
    assert expose_unit(copy.deepcopy(data_x_up), 'up', 4, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', 'F', 'F'],
            ['W', '', '', '', 'E', 'F'],
            ['X', 'X', 'X', 'X', 'X', 'X']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [4, 4]},
            {'tile': 'F', 'old_pos': [4, 4], 'new_pos': [3, 4]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'up', 5, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', 'F'],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'E']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [5, 5]},
            {'tile': 'F', 'old_pos': [5, 5], 'new_pos': [4, 5]},
            {'tile': 'F', 'old_pos': [4, 5], 'new_pos': [3, 5]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'up', 0, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['W', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['A', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [5, 0]},
            {'tile': 'W', 'old_pos': [5, 0], 'new_pos': [4, 0]},
            {'tile': 'W', 'old_pos': [4, 0], 'new_pos': [3, 0]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'up', 1, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', 'W', '', '', '', 'F'],
            ['W', 'A', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [5, 1]},
            {'tile': 'W', 'old_pos': [5, 1], 'new_pos': [4, 1]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'up', 2, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', 'A', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [5, 2]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'up', 3, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', 'A', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [5, 3]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'up', 4, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', 'F', 'F'],
            ['W', 'W', '', '', 'A', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [5, 4]},
            {'tile': 'F', 'old_pos': [5, 4], 'new_pos': [4, 4]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'up', 5, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', 'F'],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'A']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [5, 5]},
            {'tile': 'F', 'old_pos': [5, 5], 'new_pos': [4, 5]},
            {'tile': 'F', 'old_pos': [4, 5], 'new_pos': [3, 5]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'button', 0, 'earth') == {
        "field": [
            ['E', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['F', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [0, 0]},
            {'tile': 'F', 'old_pos': [0, 0], 'new_pos': [1, 0]},
            {'tile': 'F', 'old_pos': [1, 0], 'new_pos': [2, 0]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'button', 1, 'earth') == {
        "field": [
            ['F', 'E', '', '', 'W', 'W'],
            ['F', 'F', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [0, 1]},
            {'tile': 'F', 'old_pos': [0, 1], 'new_pos': [1, 1]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'button', 2, 'earth') == {
        "field": [
            ['F', 'F', 'E', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [0, 2]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'button', 3, 'earth') == {
        "field": [
            ['F', 'F', '', 'E', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [0, 3]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'button', 4, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'E', 'W'],
            ['F', '', '', '', 'W', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [0, 4]},
            {'tile': 'W', 'old_pos': [0, 4], 'new_pos': [1, 4]}
        ]
    }
    assert expose_unit(copy.deepcopy(data_x_button), 'button', 4, 'earth') == {
        "field": [
            ['X', 'X', 'X', 'X', 'X', 'X'],
            ['F', 'F', '', '', 'E', 'W'],
            ['F', '', 'F', 'W', 'W', 'W'],
            ['', '', 'W', 'F', '', 'E'],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [1, 4]},
            {'tile': 'W', 'old_pos': [1, 4], 'new_pos': [2, 4]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'button', 5, 'earth') == {
        "field": [
            ['F', 'F', '', '', 'W', 'E'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', 'W'],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'E', 'old_pos': None, 'new_pos': [0, 5]},
            {'tile': 'W', 'old_pos': [0, 5], 'new_pos': [1, 5]},
            {'tile': 'W', 'old_pos': [1, 5], 'new_pos': [2, 5]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'button', 0, 'air') == {
        "field": [
            ['A', 'F', '', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['F', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [0, 0]},
            {'tile': 'F', 'old_pos': [0, 0], 'new_pos': [1, 0]},
            {'tile': 'F', 'old_pos': [1, 0], 'new_pos': [2, 0]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'button', 1, 'air') == {
        "field": [
            ['F', 'A', '', '', 'W', 'W'],
            ['F', 'F', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [0, 1]},
            {'tile': 'F', 'old_pos': [0, 1], 'new_pos': [1, 1]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'button', 2, 'air') == {
        "field": [
            ['F', 'F', 'A', '', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [0, 2]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'button', 3, 'air') == {
        "field": [
            ['F', 'F', '', 'A', 'W', 'W'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [0, 3]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'button', 4, 'air') == {
        "field": [
            ['F', 'F', '', '', 'A', 'W'],
            ['F', '', '', '', 'W', 'W'],
            ['', '', 'F', 'W', '', ''],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [0, 4]},
            {'tile': 'W', 'old_pos': [0, 4], 'new_pos': [1, 4]}
        ]
    }
    assert expose_unit(copy.deepcopy(data), 'button', 5, 'air') == {
        "field": [
            ['F', 'F', '', '', 'W', 'A'],
            ['F', '', '', '', '', 'W'],
            ['', '', 'F', 'W', '', 'W'],
            ['', '', 'W', 'F', '', ''],
            ['W', '', '', '', '', 'F'],
            ['W', 'W', '', '', 'F', 'F']
        ],
        'move': [
            {'tile': 'A', 'old_pos': None, 'new_pos': [0, 5]},
            {'tile': 'W', 'old_pos': [0, 5], 'new_pos': [1, 5]},
            {'tile': 'W', 'old_pos': [1, 5], 'new_pos': [2, 5]}
        ]
    }

