from services import response_cep
import requests
import logging


def get_header():
    return {
        'Content-Type': 'application/json'
    }


def save(payload):
    response = None

    try:
        state = 'SP'
        city = 'São Paulo'
        adress = ''

        cep = response_cep.get_cep(state=state, city=city, adress=adress)
        print(cep)

        headers = get_header()
        logging.info('Enviando requisição para api ...')
        response = requests.post('http://localhost:8080/servico/v1/pedidos',
                                 json=payload,
                                 headers=headers)

        response.raise_for_status()
        
        logging.info('Requisição enviada com sucesso.')
        logging.info(response.json())

        return response
    except requests.exceptions.RequestException as e:
        if response is not None:

            if response.status_code != (500):
                raise Exception(response.json())
            else:
                raise Exception(f'Erro ao enviar requisição para api.{e}')

        else:
            raise Exception(f'Erro ao enviar requisição para api.{e}')
