"""

Проверка уничтожения элементов поля
И возврат новой позиции на поле

"""


def destroy_field(field, save_field=True):

    destroy_tile = {
        'route': [],
    }

    for i in range(5):
        if all(field[i]):
            set_field_up = set(field[i])
            if "X" in set_field_up:
                set_field_up.remove('X')
                if not len(set_field_up):
                    continue
            if len(set_field_up) == 1:
                field[i] = ['X', 'X', 'X', 'X', 'X', 'X']
                destroy_tile['route'].append({
                    "route": "button", "index": i
                })
                break
            else:
                break
        else:
            break

    for i in range(5, -1, -1):
        if all(field[i]):
            set_field_button = set(field[i])
            if "X" in set_field_button:
                set_field_button.remove('X')
                if not len(set_field_button):
                    continue
            if len(set_field_button) == 1:
                field[i] = ['X', 'X', 'X', 'X', 'X', 'X']
                destroy_tile['route'].append({
                    "route": "up", "index": i
                })
                break
            else:
                break
        else:
            break

    for i in range(5):
        field_left = list(_field[i] for _field in field)
        if all(field_left):
            set_field_left = list(set(field_left))
            if 'X' in set_field_left:
                set_field_left.remove('X')
                if not len(set_field_left):
                    continue
            if len(set_field_left) == 1:
                for _field in field:
                    _field[i] = 'X'
                destroy_tile['route'].append({
                    "route": "right", "index": i
                })
                break
            else:
                break
        else:
            break

    for i in range(5, -1, -1):
        field_right = list(_field[i] for _field in field)
        if all(field_right):
            set_field_right = list(set(field_right))
            if 'X' in set_field_right:
                set_field_right.remove('X')
                if not len(set_field_right):
                    continue
            if len(set_field_right) == 1:
                for _field in field:
                    _field[i] = 'X'
                destroy_tile['route'].append({
                    "route": "left", "index": i
                })
                break
            else:
                break
        else:
            break

    if destroy_tile['route']:
        destroy = destroy_field(field, False)
        if destroy['route']:
            destroy_tile['destroy'] = destroy

    if save_field:
        return {
            'destroy': destroy_tile,
            'field': field
        }

    return destroy_tile
