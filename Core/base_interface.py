# core/interfaces/base_interface.py
from abc import ABC, abstractmethod
from typing import Dict, Any, Callable
import os
import copy
import json
from utils import get_logger


class BaseInterface(ABC):
    """
    Абстрактный базовый интерфейс для всех моделей.
    Обеспечивает:
    - Единый механизм загрузки конфига
    - Lazy loading
    - Hot-reload
    - Безопасность (дефолты при ошибках)
    """
    _config_loader_cache: Dict[str, Dict[str, Any]] = {}

    def __init__(self, config_path: str = None):
        self._config = None
        self._config_path = None
        self._last_modified = None
        self.logger = get_logger()
        if config_path:
            self.set_config_path(config_path)

    def set_config_path(self, config_path: str):
        """Установка пути к конфигу (можно менять на лету)"""
        self._config_path = config_path
        self._config = None  # Сбросим кэш
        self.logger.info(f'Current config path: {self._config_path}')

    @property
    def config(self) -> Dict[str, Any]:
        """Ленивая загрузка конфига"""
        if self._config is None and self._config_path:
            self._load_config()
            self.logger.info(f"Loaded config: {self._config}")
        return self._config or self._get_default_config()

    def _load_config(self):
        """Загрузка и валидация конфига"""
        try:
            # Проверяем, изменился ли файл
            if os.path.exists(self._config_path):
                stat = os.stat(self._config_path)
                if (self._last_modified == stat.st_mtime and
                    self._config_path in self._config_loader_cache):
                    self._config = copy.deepcopy(self._config_loader_cache[self._config_path])
                    return
            else:
                self.logger.error(f"Config file not found: {self._config_path}")
                raise FileNotFoundError(f"Config file not found: {self._config_path}")

            # Загружаем JSON
            with open(self._config_path, 'r', encoding='utf-8') as f:
                raw_data = f.read()
                data = json.loads(raw_data)

            # Валидация (делегируется наследнику)
            validated = self._validate_config(data)

            # Кэшируем
            self._config_loader_cache[self._config_path] = validated
            self._config = copy.deepcopy(validated)
            self._last_modified = stat.st_mtime

        except Exception as e:
            self.logger.error(f"[Config] Load failed: {e}")
            self._config = self._get_default_config()
            self.logger.warning("Using default config due to load failure")

    def reload_config(self):
        """Принудительная перезагрузка конфига"""
        self.logger.info("Reloading config...")
        self._config = None
        self._last_modified = None
        old_path = self._config_path
        self._config_path = None
        if old_path:
            self.set_config_path(old_path)
            _ = self.config  # Триггерим загрузку
            self.logger.info("Config reloaded successfully")

    @abstractmethod
    def _validate_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Метод валидации, реализуется в наследниках"""
        pass

    @abstractmethod
    def _get_default_config(self) -> Dict[str, Any]:
        """Дефолтные значения, реализуется в наследниках"""
        pass

    @abstractmethod
    def save_project(self, filepath: str):
        """Сохранение проекта — должен быть у всех"""
        pass

    @abstractmethod
    def load_project(self, filepath: str):
        """Загрузка проекта — должен быть у всех"""
        pass