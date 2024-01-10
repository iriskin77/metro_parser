#### Парсер для продуктового маркетплейса https://online.metro-cc.ru

#### Установка

+ Клонировать репозиторий 

+ Установить виртуальное окружение

    + python -m venv venv
    + .\venv\Scripts\activate (for windows)
    + source venv/biv/activate (for linux)


+ Запустить командой python3 main.py

#### Описание

Парсер делает запрос на api сервера, откуда приходят данные на сайт https://online.metro-cc.ru.
В качестве ответа парсер получает ответ в формате json. Далее извлекаются следующие данные:

- id 
- name
- url
- rating
- price
- promo-price

Эта данные записываются в формат json и сохраняются в папку data. Пример сохраненных данных:

``````json

[
    {
        "article": 400891,
        "name": "Шоколадное яйцо Kinder Surprise Maxi, 100г",
        "url": "https://online.metro-cc.ru/products/yajco-kinder-syurpriz-maxi-iz-molochnogo-shokolada-c-molochnym-vnutrennim-sloem-igrushkoj-vnutri-liga-spravedlivosti-100g",
        "rating": 5,
        "current_price": 329,
        "disc_price": 449
    },
    {
        "article": 226825,
        "name": "Набор подарочный M&M's кондитерский Сани, 280г",
        "url": "https://online.metro-cc.ru/products/280g-podarochnyy-konditerskiy-nabor-mms-sani",
        "rating": 0,
        "current_price": 299,
        "disc_price": 449
    }
]
``````
