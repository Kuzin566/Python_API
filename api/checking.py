from requests import Response


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert response.status_code == status_code
        print("Статус код верный : " + str(status_code))

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = response.json()
        assert list(token) == expected_value
        print("Все поля присутствуют")

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        assert response.json().get(field_name) == expected_value
        print(f"{field_name} верен : " + expected_value)