from dataclasses import dataclass


@dataclass
class BaseList:
    name: str = 'base'
    elements: list = ()

    @classmethod
    def imports(cls, elements: str) -> 'BaseList':
        """Импорт базовых односимвольных элементов из базы данных

        Args:
             elements: Список элементов
        """
        return cls(elements=list(elements.replace(f"{cls.name};", '')))

    def export(self):
        """Экспорт элементов"""
        return f"{self.name}:{''.join(self.elements)}"