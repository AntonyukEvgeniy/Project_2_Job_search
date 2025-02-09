from abc import ABC, abstractmethod
from typing import Dict, List

import requests


class API(ABC):
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    @abstractmethod
    def _connect(self) -> bool:
        """Метод для подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, params: Dict = None) -> List[Dict]:
        """Метод для получения вакансий"""
        pass
