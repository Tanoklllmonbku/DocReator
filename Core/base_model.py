# core/base_model.py
from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseModel(ABC):
    """
    Абстрактная базовая модель.
    Все модели (TextModel, DiagramModel) должны наследовать от неё.
    """
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Преобразование в словарь для сериализации"""
        pass

    @abstractmethod
    def from_dict(self, data: Dict[str, Any]) -> 'BaseModel':
        """Создание модели из словаря"""
        pass

    def validate(self) -> bool:
        """Проверка корректности данных (можно переопределить)"""
        return True

    def __repr__(self):
        return f"<{self.__class__.__name__}>"