from src.json_file_handler import JSONFileHandler


class Vacancy:
    __slots__ = ('id', 'title', 'salary', 'employer', 'location')

    def __init__(self, vacancy_data: dict):
        self.__validate_vacancy_data(vacancy_data)
        self.id = vacancy_data['id']
        self.title = vacancy_data['name']
        self.salary = self.__parse_salary(vacancy_data.get('salary'))
        self.employer = vacancy_data['employer']['name']
        self.location = vacancy_data['area']['name']

    @staticmethod
    def __validate_vacancy_data(vacancy_data: dict) -> None:
        """Валидация входных данных"""
        required_fields = ['id', 'name', 'employer', 'area']
        if not all(field in vacancy_data for field in required_fields):
            raise ValueError("Отсутствуют обязательные поля в данных вакансии")

    @staticmethod
    def __parse_salary(salary_data: dict) -> int:
        """Приватный метод для обработки зарплаты"""
        if not salary_data:
            return 0
        return salary_data.get('from', 0) or salary_data.get('to', 0)

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def validate_vacancy_data_test(self, data):
        return self.__validate_vacancy_data(data)

    def parse_salary_test(self, salary_data):
        return self.__parse_salary(salary_data)

if __name__ == '__main__':
    handler = JSONFileHandler()
    data = handler.read_data()
    vacancy = Vacancy(data[0])
    print(vacancy.title)
    vacancy.validate_vacancy_data_test(data[0])
    print(vacancy.parse_salary_test(data[0]['salary']))

