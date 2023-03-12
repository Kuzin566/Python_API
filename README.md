## Настройка окружения
Для запуска тестов необходимо в файлу api_config.py переопределить директорию path_file


запускаем тесты:
* Все тесты: ```pytest```  
* Все тесты в директории: ```pytest test_api/```                           
* Конкретный тест: ```pytest test_api/test_add_name_personage_in_file.py```
* Запуск тестов чтобы сгенерировать отчет Allure ```pytest --alluredir=runtime/results```
* Просмотр отчетов ```allure serve runtime/results/```

