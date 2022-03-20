import json


def open_payload():
    with open('app/assets/order.json', encoding='utf-8') as file:
        payload = json.load(file)

    return payload
