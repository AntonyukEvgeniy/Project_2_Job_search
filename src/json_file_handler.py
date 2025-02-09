import json
from pathlib import Path

from src.base_file_handler import AbstractFileHandler
from src.hh_api import HeadHunterAPI


class JSONFileHandler(AbstractFileHandler):
    def __init__(self, filename: str = "vacancies.json"):
        data_folder = Path(__file__).parent.parent / "data"
        # Создаём директорию data, если она не существует
        data_folder.mkdir(exist_ok=True)
        file_to_open = data_folder / filename
        self.__filename = file_to_open

    def add_data(self, data: list[dict]) -> None:
        existing_data = self.read_data()
        # Удаление дублей по id вакансии
        existing_ids = {item["id"] for item in existing_data}
        new_data = [item for item in data if item["id"] not in existing_ids]

        with open(self.__filename, "a", encoding="utf-8") as file:
            json.dump(new_data, file, ensure_ascii=False, indent=2)

    def delete_data(self, criteria):
        data = self.read_data()
        filtered_data = [item for item in data if not all(item.get(key) == value for key, value in criteria.items())]

        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(filtered_data, file, ensure_ascii=False, indent=2)

    def read_data(self) -> list[dict]:
        if not Path.exists(self.__filename):
            return []
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    handler = JSONFileHandler()
    if hh_api._connect():
        print("Успешное подключение к API HeadHunter")
    else:
        print("Не удалось подключиться к API HeadHunter")
    get_vacancies = hh_api.get_vacancies({"text": "Python Developer"})
    handler.add_data(get_vacancies)
    data = handler.read_data()
    print(data)
