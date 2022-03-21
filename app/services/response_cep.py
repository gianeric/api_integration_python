from services import get_secret_manager
import requests
import logging


def get_header():
    return {
        'Content-Type': 'application/json'
    }


def get_cep(state, city, adress):
    response = None
    auth = False

    try:
        auth = get_secret_manager.auth()
        if auth == True:
            headers = get_header()
            logging.info('Enviando requisição para api ...')
            response = requests.get(f'http://viacep.com.br/ws/{state}/{city}/{adress}/json',
                                    headers=headers)

            response.raise_for_status()
            
            logging.info('Requisição enviada com sucesso.')
            logging.info(response.json())
        else:
            logging.info('Usuário não autorizado a consultar cep.')
            print('Usuário não autorizado a consultar cep.')

        return response
    except requests.exceptions.RequestException as e:
        if response is not None:

            if response.status_code != (500):
                raise Exception(response.json())
            else:
                raise Exception(f'Erro ao obter o cep.{e}')

        else:
            raise Exception(f'Erro ao obter o cep.{e}')
