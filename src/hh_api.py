from base_api import API
from typing import Dict, List


class HeadHunterAPI(API):
    def __init__(self):
        super().__init__("https://api.hh.ru")
        self.__session = self.session  # приватный атрибут для сессии
        self.__base_url = self.base_url  # приватный атрибут для базового URL

    def _connect(self) -> bool:
        try:
            response = self.__session.get(f"{self.__base_url}/ping")
            return response.status_code == 200
        except Exception:
            return False

    def get_vacancies(self, params: Dict = None) -> List[Dict]:
        if not self._connect():  # использование приватного метода
            return []
        if params is None:
            params = {}

        default_params = {"order_by": "salary_desc", "per_page": 100}
        params = {**default_params, **params}

        try:
            response = self.session.get(f"{self.base_url}/vacancies", params=params)
            if response.status_code == 200:
                return response.json()["items"]
            return []
        except Exception as e:
            print(f"Ошибка при получении вакансий: {e}")
            return []


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    if hh_api._connect():
        print("Успешное подключение к API HeadHunter")
    else:
        print("Не удалось подключиться к API HeadHunter")
    get_vacancies = hh_api.get_vacancies({"text": "Python Developer"})
    print(get_vacancies)
    print(len(get_vacancies))
    for vac in get_vacancies:
        print(vac["name"])
