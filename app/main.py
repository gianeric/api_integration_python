from services.aws import request_order
from services.aws import open_payload_order
from services.aws import send_order_sqs
from services.aws import receive_order_sqs
from views import order_view


def main():
    payload = open_payload_order.open_payload()
    request_order.save(payload)
    send_order_sqs.send(payload)
    receive_order_sqs.receive()
    order_view.save_order_graph(payload)


if __name__ == "__main__":
    main()
