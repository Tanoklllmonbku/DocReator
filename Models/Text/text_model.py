# core/models/text/text_model.py
from typing import Dict, Any, List
from Core.base_model import BaseModel
from Elements import TextElement


class TextModel(BaseModel):
    """
    Модель текстового документа.
    """
    def __init__(self, name: str = "Новый документ"):
        self.name = name
        self.elements: List[TextElement] = []

    def add_element(self, element: TextElement):
        self.elements.append(element)

    def remove_element(self, element_id: str):
        self.elements = [el for el in self.elements if el.id != element_id]

    def get_element(self, element_id: str) -> TextElement:
        for el in self.elements:
            if el.id == element_id:
                return el
        raise KeyError(f"Element {element_id} not found")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "elements": [el.to_dict() for el in self.elements]
        }

    def from_dict(self, data: Dict[str, Any]) -> 'TextModel':
        self.name = data["name"]
        self.elements = [TextElement.from_dict(el) for el in data.get("Elements", [])]
        return self