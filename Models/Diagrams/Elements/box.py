# core/models/diagram/elements/box.py
from typing import Dict, Any
from Core.base_element import BaseElement


class Box(BaseElement):
    """
    Элемент 'коробка' для диаграммы.
    Поддерживает текст, позицию, размер и стиль.
    """
    def __init__(
        self,
        text: str = "",
        x: int = 0,
        y: int = 0,
        width: int = 100,
        height: int = 50,
        font: str = "Arial",
        font_size: int = 12,
        text_color: str = "#000000",
        bg_color: str = "#FFFFFF",
        border_color: str = "#000000"
    ):
        super().__init__(element_type="box")
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.font_size = font_size
        self.text_color = text_color
        self.bg_color = bg_color
        self.border_color = border_color

    @property
    def visual_style(self) -> Dict[str, Any]:
        return {
            "font": self.font,
            "font_size": self.font_size,
            "text_color": self.text_color,
            "bg_color": self.bg_color,
            "border_color": self.border_color
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "text": self.text,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "font": self.font,
            "font_size": self.font_size,
            "text_color": self.text_color,
            "bg_color": self.bg_color,
            "border_color": self.border_color
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Box':
        return cls(
            text=data["text"],
            x=data["x"],
            y=data["y"],
            width=data["width"],
            height=data["height"],
            font=data.get("font", "Arial"),
            font_size=data.get("font_size", 12),
            text_color=data.get("text_color", "#000000"),
            bg_color=data.get("bg_color", "#FFFFFF"),
            border_color=data.get("border_color", "#000000")
        )