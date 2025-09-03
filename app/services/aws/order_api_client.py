import requests

class OrderApiClient:
    def __init__(self, logger):
        self.logger = logger

    def build_headers(self):
        return {
            'Content-Type': 'application/json'
        }

    def call_api(self, payload):
        self.logger.info("[order_api_client] Iniciando requisição para api pedidos.")
        headers = self.build_headers()
        try:
            response = requests.post('http://localhost:8082/servico/v1/pedidos',
                                    json=payload,
                                    headers=headers)

            response.raise_for_status()
            
            self.logger.info("[order_api_client] Requisição para api pedidos enviada com sucesso.", response=response.json())
            return response.json()
        except requests.Timeout as e:
            self.logger.error("[order_api_client] Timeout", error=str(e))
            raise
        except requests.ConnectionError as e:
            self.logger.error("[order_api_client] ConnectionError", error=str(e))
            raise
        except requests.HTTPError as e:
            self.logger.error(
                "[order_api_client] HTTPError", 
                payload=payload, 
                status_code=e.response.status_code,
                response=e.response.text
            )
            raise
        except requests.RequestException as e:
            self.logger.error("[order_api_client] Erro ao enviar requisição para api.", error=str(e))
            raise
