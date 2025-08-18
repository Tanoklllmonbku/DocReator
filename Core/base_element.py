# core/base_element.py
import uuid
from abc import ABC, abstractmethod
from typing import Dict, Any
from utils.logger import get_logger


class BaseElement(ABC):
    """
    Базовый элемент с ID и визуальными свойствами.
    Наследуется всеми элементами: Box, TextElement, Line и др.
    """
    def __init__(self, element_type: str):
        self.id: str = str(uuid.uuid4())
        self.type: str = element_type  # 'box', 'text', 'line' и т.д.

    @property##
    @abstractmethod
    def visual_style(self) -> Dict[str, Any]:
        """Возвращает визуальные свойства (цвет, шрифт и т.д.)"""
        pass

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Сериализация в словарь"""
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseElement':
        """Десериализация из словаря"""
        pass

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"