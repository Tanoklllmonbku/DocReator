# Interfaces/diagram_interface.py
from typing import Dict, Any
from Models.Diagrams.diagram_model import DiagramModel, Box, Line
import json
import os
from utils import get_logger
from Core import BaseInterface
from Models.Diagrams.config_schema import validate_diagram_config

class DiagramInterface(BaseInterface):
    def __init__(self, config_path: str = None):
        super().__init__(config_path)
        self.model = DiagramModel()
        self.logger = get_logger()

    def _validate_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        return validate_diagram_config(config)

    def _get_default_config(self) -> Dict[str, Any]:
        self.logger.info("Getting default diagram config")
        return {
            'default_width': 100,
            'default_height': 50,
            'grid_size': 10,
            'bg_color': '#FFFFFF'
        }

    def save_project(self, filepath: str):
        data = {
            "type": "diagram",
            "version": "1.0",
            "data": self.model.to_dict()
        }
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        self.logger.info("Saved diagram to %s", filepath)

    def load_project(self, filepath: str):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if data.get("type") != "diagram":
                raise ValueError("Not a diagram project")
            self.model.from_dict(data["data"])
            self.logger.info("Loaded diagram from %s", filepath)
        except Exception as e:
            self.logger.error(f"Failed to load project {filepath}: {e}")
            raise