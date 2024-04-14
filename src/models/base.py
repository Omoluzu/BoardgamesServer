from typing import Collection, List
from dataclasses import dataclass, field


@dataclass
class BaseList:
    """Базовая модель работы с группой элементов клиент серверного приложения.
    Работает с односимвольными элементами и абстрагирует метода получения
        и изъятия информации о конкретном списке элементов игры из csv файла игры

    Attributes:
        name: Наименования группы элементов
        elements: Список элементов

    """
    name: str = 'base'
    elements: List[str] = field(default_factory=list)

    @classmethod
    def new(cls) -> 'BaseList':
        """Создание пустой группы элементов игры

        Returns:
            Инициализированный класс с пустой группой элементов
        """
        return cls()

    @classmethod
    def imports(cls, elements: str) -> 'BaseList':
        """Импорт базовых односимвольных элементов из базы данных

        Args:
             elements: Группа элементов

        Returns:
            Инициализированный класс с группой элементов из csv
        """
        return cls(elements=list(elements.replace(f"{cls.name}:", '')))

    def export(self) -> str:
        """Экспорт элементов для сохранения в csv

        Returns:
            'name:join(elements)'
        """
        return f"{self.name}:{''.join(self.elements)}"

    def element_add(self, element: str) -> None:
        """Добавление элемента в конец списка элементов

        Args:
            element: Элемент для добавления
        """
        self.elements.extend(list(element))
