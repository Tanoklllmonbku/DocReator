# core/models/diagram/diagram_model.py
from typing import Dict, Any, List
from Core.base_model import BaseModel
from Core.base_element import BaseElement
from Elements import Box
from Elements import Line


class DiagramModel(BaseModel):
    """
    Модель диаграммы — контейнер для элементов.
    """
    def __init__(self, name: str = "Новая диаграмма"):
        self.name = name
        self.elements: List[BaseElement] = []

    def add_element(self, element: BaseElement):
        self.elements.append(element)

    def remove_element(self, element_id: str):
        self.elements = [el for el in self.elements if el.id != element_id]

    def get_element(self, element_id: str) -> BaseElement:
        for el in self.elements:
            if el.id == element_id:
                return el
        raise KeyError(f"Element {element_id} not found")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "elements": [el.to_dict() for el in self.elements]
        }

    def from_dict(self, data: Dict[str, Any]) -> 'DiagramModel':
        self.name = data["name"]
        self.elements = []

        for el_data in data.get("Elements", []):
            el_type = el_data["type"]
            if el_type == "box":
                element = Box.from_dict(el_data)
            elif el_type == "line":
                element = Line.from_dict(el_data)
            else:
                raise ValueError(f"Unknown element type: {el_type}")
            self.elements.append(element)
        return self