import json
import requests
from pathlib import Path
from src.params import url, headers, cookies, json_data


def get_path():
    abs_path = Path(__file__).resolve().parent.parent
    return abs_path


def make_request(url, headers, cookies, json_data) -> dict | str:
    response = requests.post(url=url, cookies=cookies, headers=headers, json=json_data)
    if response.status_code == 200:
        return response.json()
    else:
        return f'Bad request: {response.status_code}'


def parse_data(metro_items: dict) -> list[dict]:

    res = []
    metro_url = 'https://online.metro-cc.ru'

    try:
        for item in metro_items['data']['category']['products']:

            dct = {}

            dct['article'] = item['article']
            dct['name'] = item['name']
            dct['url'] = metro_url + item['url']
            dct['rating'] = item['rating']

            for price in item['stocks']:

                dct['current_price'] = price['prices_per_unit']['offline']['price']
                dct['disc_price'] = price['prices_per_unit']['offline']['old_price']

            res.append(dct)

        return res

    except Exception as ex:
        print(f"Error has been occured: {ex}")


def wrtie_json(file_name: str, file_path, data: list[dict]) -> None:
    with open(f"{file_path}/data/{file_name}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    json_metro = make_request(url=url, headers=headers, cookies=cookies, json_data=json_data)
    data = parse_data(metro_items=json_metro)
    path = get_path()
    wrtie_json(file_name='metro_products', file_path=path, data=data)

