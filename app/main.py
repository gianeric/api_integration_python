from services import request_order
from services import open_payload_order
from services import send_order_sqs
from services import receive_order_sqs


def main():
    payload = open_payload_order.open_payload()
    response = request_order.save(payload)
    send_order_sqs.send(payload)
    receive_order_sqs.receive()


if __name__ == "__main__":
    main()
