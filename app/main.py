from services import request_order
import json


def main():
    with open('assets/order.json', encoding='utf-8') as file:
        payload = json.load(file)
    
    print(type(payload))

    request_order.save(payload)


if __name__== "__main__":
  main()