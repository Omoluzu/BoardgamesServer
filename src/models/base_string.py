from dataclasses import dataclass, field


@dataclass
class BaseString:
    element: str
    name: str = field(default='base')

    @classmethod
    def new(cls) -> 'BaseString':
        """Создание пустого строкового элемента игры

        Returns:
             Инициализированный класс с пустым строковым значением
        """
        return cls(element='')

    @classmethod
    def imports(cls, element: str) -> 'BaseString':
        """Импорт строкового элемента из csv игры

        Args:
            element: Строковый элемент
                'name:element'

        Returns:
            Инициализированный класс строкового элемента из csv
        """
        name, _element = element.split(':')

        assert name == cls.name
        return cls(element=_element)

    def export(self) -> str:
        """Экспорт игры для сохранения в csv

        Returns:
            'name:element'
        """
        return f"{self.name}:{self.element}"
