# core/models/diagram/elements/line.py
from typing import Dict, Any
from Core.base_element import BaseElement


class Line(BaseElement):
    """
    Линия между двумя блоками.
    """
    def __init__(
        self,
        start_box_id: str,
        end_box_id: str,
        label: str = "",
        color: str = "#000000",
        width: int = 1
    ):
        super().__init__(element_type="line")
        self.start_box_id = start_box_id
        self.end_box_id = end_box_id
        self.label = label
        self.color = color
        self.width = width

    @property
    def visual_style(self) -> Dict[str, Any]:
        return {
            "color": self.color,
            "width": self.width
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "start_box_id": self.start_box_id,
            "end_box_id": self.end_box_id,
            "label": self.label,
            "color": self.color,
            "width": self.width
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Line':
        return cls(
            start_box_id=data["start_box_id"],
            end_box_id=data["end_box_id"],
            label=data.get("label", ""),
            color=data.get("color", "#000000"),
            width=data.get("width", 1)
        )