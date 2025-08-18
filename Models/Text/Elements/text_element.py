# core/models/text/elements/text_element.py
from typing import Dict, Any
from Core.base_element import BaseElement


class TextElement(BaseElement):
    """
    Текстовый элемент с форматированием.
    """
    def __init__(
        self,
        text: str = "",
        font: str = "Arial",
        size: int = 12,
        color: str = "#000000",
        bold: bool = False,
        italic: bool = False
    ):
        super().__init__(element_type="text")
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.bold = bold
        self.italic = italic

    @property
    def visual_style(self) -> Dict[str, Any]:
        return {
            "font": self.font,
            "size": self.size,
            "color": self.color,
            "bold": self.bold,
            "italic": self.italic
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "text": self.text,
            "font": self.font,
            "size": self.size,
            "color": self.color,
            "bold": self.bold,
            "italic": self.italic
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TextElement':
        return cls(
            text=data["text"],
            font=data.get("font", "Arial"),
            size=data.get("size", 12),
            color=data.get("color", "#000000"),
            bold=data.get("bold", False),
            italic=data.get("italic", False)
        )