from services.aws.order_graph import OrderGraph


def save_order_graph(payload):
    order_graph = OrderGraph()
    order_graph.save(payload)
