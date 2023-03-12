import allure
from api.swapi_dev import Swapi_dev_api
from list_and_description.list_personage import dart_vader

@allure.description("Создаем список персножаей, которые снимались в фильмах с нашим персонажем")
def test_add_name_personage_in_file():
    sda = Swapi_dev_api()
    sda.create_list_filmed_personage(dart_vader)



