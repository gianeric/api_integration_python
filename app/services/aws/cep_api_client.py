from services.aws.secrets_authenticator import SecretsAuthenticator
import requests

class CepApiClient:
    def __init__(self, logger):
        self.logger = logger

    def build_headers(self):
        return {
            'Content-Type': 'application/json'
        }

    def get_cep(self, state, city, address):
        self.logger.info("[cep_api_client] Iniciando requisição para api cep.")
        response = None
        try:
            secret_client = SecretsAuthenticator(self.logger)
            auth = secret_client.auth()

            if auth:
                headers = self.build_headers()

                response = requests.get(
                    f'http://viacep.com.br/ws/{state}/{city}/{address}/json',
                    headers=headers
                )
                response.raise_for_status()

                self.logger.info("[cep_api_client] Requisição enviada com sucesso.", response=response.json())
                return response.json()
            else:
                self.logger.info("[cep_api_client] Usuário não autorizado a consultar cep.")
                return None
        except requests.exceptions.HTTPError as e:
            self.logger.error("[cep_api_client] HTTP error occurred.", error=str(e))
            if response is not None and response.status_code != 500:
                raise Exception(response.json())
            else:
                raise Exception("Erro ao obter o cep.", e)
        except requests.exceptions.ConnectionError as e:
            self.logger.error("[cep_api_client] Connection error occurred.", error=str(e))
            raise
        except requests.exceptions.Timeout as e:
            self.logger.error("[cep_api_client] Timeout error occurred.", error=str(e))
            raise
        except requests.exceptions.RequestException as e:
            self.logger.error("[cep_api_client] Request exception occurred.", error=str(e))
            if response is not None and response.status_code != 500:
                raise Exception(response.json())
            else:
                raise Exception("Erro ao obter o cep.", e)
        except Exception as e:
            self.logger.error("[cep_api_client] Unexpected error occurred.", error=str(e))
            raise
