from services import request_order
from services import open_payload_order


def main():
    payload = open_payload_order.open_payload()
    response = request_order.save(payload)
    print(response.json())


if __name__ == "__main__":
    main()
