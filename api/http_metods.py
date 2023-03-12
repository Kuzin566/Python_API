import requests


class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):
        print(url)
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return result
