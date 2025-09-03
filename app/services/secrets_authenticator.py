import boto3
import botocore.exceptions
import json 

class SecretsAuthenticator:
    def __init__(self, logger):
        self.logger = logger

    def auth(self):
        self.logger.info("[secrets_authenticator] Iniciando autenticação via AWS Secrets Manager.")
        try:
            client = boto3.client('secretsmanager',
                                region_name='sa-east-1',
                                endpoint_url='http://localhost:4566'
                                )

            response = client.get_secret_value(
                SecretId='ApiIntegrationPython'
            )

            database_secrets = json.loads(response['SecretString'])
            self.logger.info("[secrets_authenticator] Secret value recebido.")

            if database_secrets['password'] == '1234':
                return True
            else:
                return False
        except botocore.exceptions.ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'ResourceNotFoundException':
                self.logger.info("[secrets_authenticator] Secret não encontrado", error=str(e))
            else:
                self.logger.info("[secrets_authenticator] Ocorreu um erro ao extrair informações do secret", error=str(e))
            raise
