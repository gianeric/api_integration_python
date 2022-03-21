import boto3
import botocore.exceptions
import json 
import logging


def auth():
    try:
        logging.info('Extraindo valor da secret...')
        client = boto3.client('secretsmanager',
                              region_name='sa-east-1',
                              endpoint_url='http://localhost:4566'
                              )

        response = client.get_secret_value(
            SecretId='ApiIntegrationPython'
        )

        database_secrets = json.loads(response['SecretString'])
        logging.info('Secret value recebido.')

        if database_secrets['password'] == '1234':
            return True
        else:
            return False
    except botocore.exceptions.ClientError as e:
        logging.info(f'Ocorreu um erro ao extrair informações do secret. {e}')
        raise(f'Ocorreu um erro ao extrair informações do secret. {e}')