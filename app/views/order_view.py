from app.services.order_graph_repository import OrderGraph


def save_order_graph(payload):
    order_graph = OrderGraph()
    order_graph.save(payload)
