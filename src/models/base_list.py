from typing import List, Optional
from dataclasses import dataclass, field
from copy import copy

from src import models



@dataclass
class BaseList:
    """Базовая модель работы с группой элементов клиент серверного приложения.
    Работает с односимвольными элементами и абстрагирует метода получения
        и изъятия информации о конкретном списке элементов игры из csv файла игры

    Attributes:
        name: Наименования группы элементов
        elements: Список элементов
        suffix: Возможность импортирования элементов, наименование которое
            может иметь некоторый суффикс.
            При установке данного параметра в True атрибут name будет
            переопределен на новый.
            По умолчанию False,
        limit: Лимит хранимых значений в атрибуте elements
        log.element_add: Список добавленных элементов
        log.element_extra: Список элементов не вошедших в атрибут element
            из-за превышенного лимита значений указанного в атрибуте limit
        log.element_clear: Список удаленных элементов.
    """
    name: str = field(default='base')
    elements: List[str] = field(default_factory=list)
    suffix: bool = field(default=False, init=False)
    limit: int = field(default=0, init=False)

    def __post_init__(self):
        self.log = models.Log()

    def __len__(self):
        return len(self.elements)

    @classmethod
    def new(cls) -> 'BaseList':
        """Создание пустой группы элементов игры

        Returns:
            Инициализированный класс с пустой группой элементов
        """
        return cls()

    @classmethod
    def imports(cls, elements: str) -> 'BaseList':
        """Импорт базовых односимвольных элементов из csv игры

        Args:
            elements: Группа элементов

        Returns:
            Инициализированный класс с группой элементов из csv
        """
        name, _elements = elements.split(':')
        _elements = list(_elements)

        if cls.suffix:
            assert name.startswith(cls.name)
            return cls(name=name, elements=_elements)

        assert name == cls.name
        return cls(elements=_elements)

    def export(self) -> str:
        """Экспорт элементов для сохранения в csv

        Returns:
            'name:join(elements)'
        """
        return f"{self.name}:{''.join(self.elements)}"

    def element_add(self, element: Optional[str]) -> None:
        """Добавление элемента в конец списка элементов

        Args:
            element: Элементы для добавления. Каждый элемент будет записан как
                отдельный.
                'x'
                'rbg'
        """
        if not element:
            return

        _element = list(element)

        if self.limit and (len(self.elements) + len(_element)) > self.limit:
            limit = self.limit - len(self.elements)
            self.log.element_extra = _element[limit:]
            _element = _element[:limit]

        self.elements.extend(_element)
        self.log.element_add = _element

    def clear(self) -> None:
        """Удаление всех элементов входящих в данной группу"""
        self.log.element_clear = copy(self.elements)
        self.elements.clear()
