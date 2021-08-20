Микросервис для электронного магазина
Модель/cущности:
Товар - отвечает за товар на складе, например - телефон такой-то марки от такого-то производителя.
Поля:
идентификатор (ID)
название
описание
параметры: массив пар ключ/значение

Сущности хранятся в MongoDB на localhost:27017

Установка: Склонируйте репозиторий Создайте и войдите в вирутальное окружение Установите зависимости: pip install -r requirements.txt

GET запрос на получение всех товаров
http://127.0.0.1:5000/

GET запрос на получение товаров по ID
URL: http://127.0.0.1:5000/<string:slug>

GET запрос на получение Товаров отсортированых по названию
URL: http://127.0.0.1:5000/?order

GET запрос на получение Отфильтрованных по названию или описанию или по id
URL: http://127.0.0.1:5000/?title=fgh&id=611fb1985fb03d5bdf5b0ff8&description=611fb1985fb03d5bdf5b0ff8
через & вводится новый параметр. При неправильном параметре выведется текст

POST запрос на создание нового товара
URL: http://127.0.0.1:5000/
QUERY PARAMETERS title, description