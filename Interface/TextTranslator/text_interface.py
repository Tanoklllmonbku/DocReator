# Interfaces/text_interface.py
from typing import Dict, Any
from Models.Text import TextModel
from Core import BaseInterface
from Models.Text.config_schema import validate_text_config
import json
import os
from utils import get_logger


class TextInterface(BaseInterface):
    def __init__(self, config_path: str = None):
        super().__init__(config_path)
        self.model = TextModel()
        self.logger = get_logger()

    def _validate_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        return validate_text_config(config)

    def _get_default_config(self) -> Dict[str, Any]:
        self.logger.info('get default config')
        return {
            'default_font': 'Arial',
            'default_size': 12,
            'default_color': '#000000'
        }


    def save_project(self, filepath: str):
        data = {
            "type": "text",
            "version": "1.0",
            "data": self.model.to_dict()
        }
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        self.logger.info('Project saved to %s', filepath)

    def load_project(self, filepath: str):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if data.get("type") != "text":
                self.logger.error(f"Invalid project type: expected 'text', got '{data.get('type')}'")
                raise ValueError("Not a text project")
            self.model.from_dict(data["data"])
            self.logger.info('Project loaded from %s', filepath)
        except Exception as e:
            self.logger.error(f"Failed to load project {filepath}: {e}")
            raise