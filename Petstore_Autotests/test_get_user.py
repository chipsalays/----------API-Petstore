import requests

headers = {
    "Content-Type": "application/json",
    "api_key": "special-key"
}

def test_1_create_user():
    print("\n[ТЕСТ 1] Создание одного пользователя (POST /user)")
    print("Отправляем запрос на создание пользователя autotestuser...")
    url = "https://petstore.swagger.io/v2/user"
    payload = {
        "id": 888,
        "username": "autotestuser",
        "firstName": "Авто",
        "lastName": "Тестов",
        "email": "auto@test.com",
        "password": "auto123",
        "phone": "1234567890",
        "userStatus": 1
    }
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("РЕЗУЛЬТАТ: УСПЕШНО - Пользователь создан")
    else:
        print(f"РЕЗУЛЬТАТ: ОШИБКА - Получен код {response.status_code}")
    
    assert response.status_code == 200

def test_2_get_existing_user():
    print("\n[ТЕСТ 2] Получение существующего пользователя (GET /user)")
    print("Ищем пользователя autotestuser...")
    url = "https://petstore.swagger.io/v2/user/autotestuser"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print(f"РЕЗУЛЬТАТ: УСПЕШНО - Пользователь найден, имя: {data.get('username')}")
    else:
        print(f"РЕЗУЛЬТАТ: ОШИБКА - Получен код {response.status_code}")
    
    assert response.status_code == 200

def test_3_create_user_list():
    print("\n[ТЕСТ 3] Создание списка пользователей (POST /user/createWithList)")
    print("Отправляем запрос на создание двух пользователей...")
    url = "https://petstore.swagger.io/v2/user/createWithList"
    payload = [
        {
            "id": 111,
            "username": "user_alpha",
            "firstName": "Альфа",
            "lastName": "Тестов",
            "email": "alpha@test.com",
            "password": "alpha123",
            "phone": "1111111111",
            "userStatus": 0
        },
        {
            "id": 222,
            "username": "user_beta",
            "firstName": "Бета",
            "lastName": "Тестова",
            "email": "beta@test.com",
            "password": "beta123",
            "phone": "2222222222",
            "userStatus": 1
        }
    ]
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("РЕЗУЛЬТАТ: УСПЕШНО - Список пользователей создан")
    else:
        print(f"РЕЗУЛЬТАТ: ОШИБКА - Получен код {response.status_code}")
    
    assert response.status_code == 200

def test_4_get_nonexistent_user():
    print("\n[ТЕСТ 4] Получение несуществующего пользователя (негативный тест)")
    print("Ищем пользователя ghostuser999 (которого не существует)...")
    url = "https://petstore.swagger.io/v2/user/ghostuser999"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 404:
        print("РЕЗУЛЬТАТ: УСПЕШНО - Сервер вернул 404, пользователь не найден")
    elif response.status_code == 200:
        print("РЕЗУЛЬТАТ: ОШИБКА - Сервер нашёл пользователя, а должен был не найти")
    else:
        print(f"РЕЗУЛЬТАТ: УСПЕШНО - Сервер вернул ошибку {response.status_code}")
    
    assert response.status_code != 200

def test_5_create_user_without_username():
    print("\n[ТЕСТ 5] Создание пользователя без обязательного поля username (негативный тест)")
    print("Отправляем JSON без поля username...")
    url = "https://petstore.swagger.io/v2/user"
    payload = {
        "id": 777,
        "firstName": "Без",
        "lastName": "Имени",
        "email": "no_name@test.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code != 200:
        print(f"РЕЗУЛЬТАТ: УСПЕШНО - Сервер отклонил запрос с кодом {response.status_code}")
    else:
        print("РЕЗУЛЬТАТ: ОБНАРУЖЕН БАГ - Сервер создал пользователя без поля username")
    
    assert response.status_code != 200

def test_6_create_user_empty_body():
    print("\n[ТЕСТ 6] Создание пользователя с пустым телом запроса (негативный тест)")
    print("Отправляем POST запрос без тела...")
    url = "https://petstore.swagger.io/v2/user"
    response = requests.post(url, headers=headers)
    
    if response.status_code != 200:
        print(f"РЕЗУЛЬТАТ: УСПЕШНО - Сервер отклонил пустой запрос с кодом {response.status_code}")
    else:
        print("РЕЗУЛЬТАТ: ОБНАРУЖЕН БАГ - Сервер принял пустой запрос")
    
    assert response.status_code != 200

def test_7_create_with_empty_list():
    print("\n[ТЕСТ 7] Создание списка с пустым массивом (негативный тест)")
    print("Отправляем пустой массив [] в createWithList...")
    url = "https://petstore.swagger.io/v2/user/createWithList"
    response = requests.post(url, json=[], headers=headers)
    
    if response.status_code != 200:
        print(f"РЕЗУЛЬТАТ: УСПЕШНО - Сервер отклонил пустой массив с кодом {response.status_code}")
    else:
        print("РЕЗУЛЬТАТ: ОБНАРУЖЕН БАГ - Сервер вернул 200 на пустой массив")
    
    assert response.status_code != 200