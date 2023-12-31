# Магазин продуктов

Это тестовое задание представляет собой проект магазина продуктов с использованием фреймворка Django и Django REST Framework (DRF). Проект включает в себя функционал создания, редактирования, удаления категорий и подкатегорий товаров в админке, а также CRUD операции для продуктов и корзины.


## Установка

1. Склонируйте репозиторий на своем компьютере:

```shell
git clone https://github.com/Pisarev82/online_store.git
```

2. Перейдите в папку проекта:

```shell
cd src
```

3. Установите зависимости:

```shell
pip install -r requirements.txt
Либо
pipenv sync
```

## Запуск сервера разработки

1. Перейдите в корневую папку проекта:

```shell
cd src
```

2. Запустите сервер разработки Django:

```shell
python manage.py runserver
```

3. Сервер будет доступен по адресу `http://localhost:8000/`.

## Использование

### Создание, редактирование и удаление категорий и подкатегорий

Админка проекта предоставляет интерфейс для управления категориями и подкатегориями товаров. Вы можете создавать, редактировать и удалять категории и подкатегории, устанавливая для них наименование, slug-имя и изображение.

### Просмотр всех категорий с подкатегориями

API-эндпоинт `/categories/` предоставляет возможность просмотра всех категорий с их подкатегориями. Результаты поддерживают пагинацию.

### Добавление, изменение и удаление продуктов

Админка проекта также позволяет добавлять, изменять и удалять продукты. Каждый продукт должен относиться к определенной подкатегории и категории, и иметь наименование, slug-имя, изображение в трех размерах и цену.

### Вывод продуктов с пагинацией

API-эндпоинт `/products/` предоставляет возможность просмотра продуктов с пагинацией. Каждый продукт в выводе содержит следующие поля: наименование, slug, категория, подкатегория, цена и список изображений.

### Управление корзиной

API-эндпоинты позволяют добавлять, изменять (количество) и удалять продукты в корзине. Также реализован эндпоинт для вывода состава корзины с подсчетом количества товаров и суммы стоимости товаров в корзине. Существует возможность полной очистки корзины.

### Авторизация

Авторизация осуществляется по токену. Авторизированный пользователь может выполнять операции связанные с корзиной только со своей корзиной.

## Технологии

Проект реализован с использованием следующих технологий:

- Django - популярный фреймворк для разработки веб-приложений на языке Python.
- Django REST Framework (DRF) - расширение Django для создания RESTful API.
- Swagger - помогает тестировать функционал, и наглядно показывает доступные методы
- SIMPLE_JWT - библиотека аутентификиции с использованием JWT токена

## Примеры запросов

### Получение всех категорий с подкатегориями

**URL:**

```
GET /categories/?limit=10&offset=1
```

**Ответ:**

```json
{
  "count": 12,
  "next": "http://127.0.0.1:8000/categories/?limit=10&offset=11",
  "previous": "http://127.0.0.1:8000/categories/?limit=10",
  "results": [
    {
      "id": 2,
      "title": "Вода",
      "parent": null,
      "slug": "voda",
      "image": null
    },
    {
      "id": 4,
      "title": "Газированная",
      "parent": 2,
      "slug": "gazirovannaia",
      "image": null
    },
    {
      "id": 5,
      "title": "Не газированная",
      "parent": 2,
      "slug": "ne-gazirovannaia",
      "image": null
    },
    {
      "id": 6,
      "title": "Сладкая",
      "parent": 2,
      "slug": "sladkaia",
      "image": null
    },
    {
      "id": 3,
      "title": "Еда",
      "parent": null,
      "slug": "eda",
      "image": null
    },
    {
      "id": 9,
      "title": "Вкусная",
      "parent": 3,
      "slug": "vkusnaia",
      "image": null
    },
    {
      "id": 7,
      "title": "Готовая",
      "parent": 3,
      "slug": "gotovaia",
      "image": null
    },
    {
      "id": 10,
      "title": "Клевая",
      "parent": 3,
      "slug": "klevaia",
      "image": null
    },
    {
      "id": 8,
      "title": "Полезная",
      "parent": 3,
      "slug": "poleznaia",
      "image": null
    },
    {
      "id": 11,
      "title": "Сладости",
      "parent": null,
      "slug": "sladosti",
      "image": null
    }
  ]
}
```

### Добавление продукта в корзину

**URL:**

```
POST /cart-item/
```

**Заголовок запроса**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4NDUwMzE3LCJpYXQiOjE2OTgzN
```

**Тело запроса:**

```json
{
  "cart": 2,
  "product": 5,
  "quantity": 5
}
```

**Ответ:**

```json
{
  "cart": 2,
  "product": 5,
  "product_name": "Мясо",
  "quantity": 5
}
```
