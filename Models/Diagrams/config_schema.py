# core/models/diagram/config_schema.py
from typing import Dict, Any

def validate_diagram_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Валидация конфига для диаграмм"""
    required = ['default_width', 'default_height', 'grid_size', 'bg_color']
    for key in required:
        if key not in config:
            raise KeyError(f"Missing required key: {key}")

    # Проверка типов
    if not isinstance(config['default_width'], int) or config['default_width'] <= 0:
        raise ValueError("default_width must be positive int")

    if not isinstance(config['default_height'], int) or config['default_height'] <= 0:
        raise ValueError("default_height must be positive int")

    if not isinstance(config['grid_size'], int) or config['grid_size'] <= 0:
        raise ValueError("grid_size must be positive int")

    if not isinstance(config['bg_color'], str):
        raise ValueError("bg_color must be string")

    # Пользователь может менять значения, но не структуру
    return {
        'default_width': config['default_width'],
        'default_height': config['default_height'],
        'grid_size': config['grid_size'],
        'bg_color': config['bg_color']
    }