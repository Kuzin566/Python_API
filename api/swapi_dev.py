import allure
from api.checking import Checking
from api.http_metods import Http_methods
from api_config import config
from object.personage import Personage


class Swapi_dev_api(Http_methods):
    project = 'swapi_dev_api'

    def __init__(self):
        self.personage = Personage()

    def get_films_personage(self, personage_id, name):
        """Метод который будет возвращать список фильмов в которых снимался определенный персонаж"""
        self.personage.id = personage_id
        resource = f'people/{self.personage.id}/'
        url = config['url'][self.project] + resource
        response = self.get(url)
        print(f"Отправили запрос на получение информации о персонаже c ID : {self.personage.id}")
        Checking.check_status_code(response, 200)
        Checking.check_json_value(response, 'name', name)
        self.personage.name = response.json().get('name')
        self.personage.list_api_films = response.json().get('films')
        self.personage.response = response
        return self.personage

    def get_list_api_personage_in_film(self):
        """Метод который будет возвращать спикок API персонажей, которые снимались вместе с нашим персонажем"""
        list_api_personage = []
        for api_films in self.personage.list_api_films:
            response = self.get(api_films)
            list_api_personage.extend(response.json().get('characters'))
        list_api_personage = list(set(list_api_personage))  # Убираем из списка повторяющиеся API персонажей
        print(f"Создали список с API персонажей, которые снимались в фильмах вместе с {self.personage.name}")
        return list_api_personage

    def get_list_personage_in_film(self):
        """Метод который будет возвращать спикос имен персонажей, которые снимались вместе с нашим персонажем"""
        list_name_connect_personage = []
        for api_personage in self.get_list_api_personage_in_film():
            response = self.get(api_personage)
            name = response.json().get('name')
            list_name_connect_personage.append(name)
        print(f"Создали список имен персонажей, которые снимались в фильмах вместе с {self.personage.name}")
        return list_name_connect_personage

    @staticmethod
    def add_name_personage_in_file(list_personage):
        """Метод, который добавит всех персонажей, снявшихся в нужных нам фильмах в файл"""
        with open(config['path_file'], 'a', encoding='utf-8') as file:
            for name in list_personage:
                file.write(f'{name}' + '\n')
                print(f"В файл добавили персонажа : {name}")

    def create_list_filmed_personage(self, personage):
        with allure.step(
                "create_list_filmed_personage: Запрашиваем список фильмов в которых снимался наш персонаж,"
                "потом смортрим всех персонажей, которые снимались в этих же фильмах и добавляем их в файл "):
            self.get_films_personage(personage_id=personage['id'], name=personage['name'])
            self.personage.list_name_connect_personage = self.get_list_personage_in_film()
            print(len(self.personage.list_name_connect_personage))
            print(self.personage.list_name_connect_personage)
            Swapi_dev_api.add_name_personage_in_file(self.personage.list_name_connect_personage)
