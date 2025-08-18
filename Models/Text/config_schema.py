# core/models/text/config_schema.py
from typing import Dict, Any

def validate_text_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Валидация конфига для текста"""
    required = ['default_font', 'default_size', 'default_color']
    for key in required:
        if key not in config:
            raise KeyError(f"Missing required key: {key}")

    if not isinstance(config['default_font'], str):
        raise ValueError("default_font must be string")

    if not isinstance(config['default_size'], int) or config['default_size'] <= 0:
        raise ValueError("default_size must be positive int")

    if not isinstance(config['default_color'], str):
        raise ValueError("default_color must be string")

    return {
        'default_font': config['default_font'],
        'default_size': config['default_size'],
        'default_color': config['default_color']
    }