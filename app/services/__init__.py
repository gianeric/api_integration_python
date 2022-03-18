from services import request_order
import json


def main():
      with open('app/util/order.json', encoding='utf-8') as file:
        order = json.load(file)
    
    print(type(order))

    payload = request_order_mapper.mapper_contract(order)
    correlationId = request_order_mapper.mapper_correlationId(order)

    # print(data2)
    request_order.save_contract(payload)


if __name__== "__main__":
  main()