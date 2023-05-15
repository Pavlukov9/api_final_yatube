# API_YATUBE
Данный проект создан в рамках учебного курса Яндекс.Правктикум.
Он представляет из себя REST API для социальной сети блогеров ***Yatube***.
Методы, которые поддерживает проект:    
:white_check_mark: GET    
:white_check_mark: POST    
:white_check_mark: PUT    
:white_check_mark: PATCH    
:white_check_mark: DELETE    

Представление данных в формате ***JSON***
____________________________

# Как запустить проект:
1. Клонируйте репозиторий с проектом:

```git clone https://github.com/Pavlukov9/api_yatube.git```

2. В созданной директории установите и активируйте виртуальное окружение, установите необходимые зависимости:

```python -m venv venv```
```source venv/Scripts/activate```
```pip install -r requirements.txt```

3. Выполните миграции:

```python manage.py migrate```

4. Создайте суперпользователя:

```python manage.py createsuperuser```

5. Запустите проект:

```python manage.py runserver```
____________________________

# Примеры запросов

Создание поста

Отправить POST-запрос на адрес `api/v1/posts/` и передать обязательное поле `text`, в заголовке указать `Authorization`:`Bearer <токен>`.

1. Пример запроса:

   ```json
   {
     "text": "Мой первый пост."
   }
   ```

2. Пример ответа:

   ```json
   {
     "id": 2,
     "author": "Dmitrii",
     "text": "Мой первый пост.",
     "pub_date": "2022-04-22T12:00:22.021094Z",
     "image": null,
     "group": null
   }
   ```

Комментирование поста пользователя

Отправить POST-запрос на адрес `api/v1/posts/{post_id}/comments/` и передать обязательные поля `post` и `text`, в заголовке указать `Authorization`:`Bearer <токен>`.

1. Пример запроса:

   ```json
   {
     "post": 1,
     "text": "Тест"
   }
   ```

2. Пример ответа:

   ```json
   {
     "id": 1,
     "author": "Dmitrii",
     "text": "Тест",
     "created": "2022-04-22T12:06:13.146875Z",
     "post": 1
   }
   ```
____________________________

Проект запустился по адресу: 
http://127.0.0.1:8000/
____________________________

