import requests
import logging


def get_header():
    return {
        'Content-Type': 'application/json'
    }


def save(payload):
    response = None

    try:
        logging.info('Enviando requisição para api ...')
        response = requests.post('http://localhost:8080/servico/v1/pedidos'
                                ,json=payload
                                ,headers=get_header())
        
        response.raise_for_status()

        return response
    except requests.exceptions.RequestException as e:
        if response != None:

            if response.status_code != (500):
                raise Exception (response.json())
            else:
                raise Exception ("Erro ao enviar requisição para api.")

        else:
            raise Exception ("Erro ao enviar requisição para api.")
