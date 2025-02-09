from abc import ABC, abstractmethod


class AbstractFileHandler(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_data(self, data):
        """Метод добавления данных в файл"""
        pass

    @abstractmethod
    def read_data(self):
        """Метод получения данных из файла"""
        pass

    @abstractmethod
    def delete_data(self, criteria):
        """Метод удаления данных из файла"""
        pass
