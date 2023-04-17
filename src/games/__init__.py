from .azul.view import started_configure as azul_start
from .ignis.view import started_configure as ignis_start


start_game = {
    'azul': azul_start,
    'ignis': ignis_start,
}
