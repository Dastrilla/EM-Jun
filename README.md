# Тестовое задание компании Effective Mobile на позицию Junior Backend Developer

Задание
----------
Разработать систему управления библиотекой

Подробное ТЗ - https://docs.google.com/document/d/1NeoX8ZxOKy7DUSo6n68y9x9EpPLYD2gGuI6CV7Osj2Y/edit?usp=sharing


Технологии
----------
Python 3.12


Установка и настройка проекта
----------
1. Клонировать репозиторий:
```bash

git clone https://github.com/Dastrilla/EM-Jun.git

```

2. Перейдите в директорию проекта для настройки, если у вас есть своя библиотека json формата: id, title, author, year, status. Вы можете ее клонировать в основную дирректорию проекта и переимновать в lib.json для использования. lib.json содержит небольшую библиотеку для примера. Если вы хотите создать свою собственную, удалите этот файл.

3. Для запуска проекта используйте app.py приложение:
```bash

python app.py

```

Функционал
----------
Разработанная система предоставляет следующие возможности:

1. Добавлять книги
2. Удалять книги
3. Искать необходимые книги по Заголовку, автору или году
4. Выводить в табличном формате всю библиотеку
5. Изменять статус книг(в наличии/выдана)
6. Завершение работы системы
