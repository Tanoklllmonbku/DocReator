# core/utils/config_loader.py
from .file_handler import FileHandler
from typing import Dict, Any, Callable
import copy


class ConfigLoader:
    """
    Универсальный загрузчик конфигов.
    Принимает путь и схему валидации.
    Не знает, что такое "diagram" или "text" — только данные.
    """
    _cache: Dict[str, Dict[str, Any]] = {}

    def __call__(
        self,
        config_path: str,
        validator: Callable[[Dict[str, Any]], Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Загружает конфиг и применяет валидатор.
        :param config_path: Путь к JSON
        :param validator: Функция/класс, проверяющий и возвращающий конфиг
        :return: Валидированный конфиг
        """
        # Кэширование
        if config_path in self._cache:
            raw_data = self._cache[config_path]
        else:
            raw_data = FileHandler.load_json(config_path)
            self._cache[config_path] = copy.deepcopy(raw_data)  # Защита от мутации

        # Валидация
        try:
            validated = validator(raw_data)
            return validated
        except Exception as e:
            raise ValueError(f"Config validation failed for {config_path}: {e}")