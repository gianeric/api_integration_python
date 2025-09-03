from configs.logger import get_logger
from services.order_api_client import OrderApiClient
from services.order_sqs_publisher import OrderSqsPublisher
from services.order_graph_repository import OrderGraphRepository
from utils import payload_loader

def main():
    logger = get_logger(None)
    logger.info("[main] Iniciando aplicação.")

    try:
        payload = payload_loader.load_payload("../app/assets/order.json")
        logger.info("[main] Payload", payload=payload)

        api_client = OrderApiClient(logger)
        api_client.call_api(payload)

        sqs_client = OrderSqsPublisher(logger)
        sqs_client.send(payload)

        # TODO: Implementar persistência do grafo do pedido, talvez usando DocumentDB futuramente.
        # graph_client = OrderGraphRepository(logger)
        # graph_client.save_order_graph(payload)
    except Exception as e:
        logger.error("[main] Erro inesperado na aplicação.", error=str(e))
        return {
            "status_code": 500,
            "body": {
                "status": "error",
                "message": str(e)
            }
        }

if __name__ == "__main__":
    main()
