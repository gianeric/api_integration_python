import boto3
import botocore.exceptions
import json 
import logging


def send(payload):
    try:
        logging.info('Enviando pedido para fila sqs...')
        sqs = boto3.client('sqs',
                           region_name='sa-east-1',
                           endpoint_url='http://localhost:4566'
                          )
        
        queue_url = 'http://localhost:4566/000000000000/sqsfilapedido'

        payload_dumps = json.dumps(payload, ensure_ascii=False)
        
        response_sqs_send = sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=10,
            MessageBody=payload_dumps,
            MessageAttributes={}
        )
        
        logging.info('Pedido enviado a fila sqs.')
        return response_sqs_send
        
    except botocore.exceptions.ClientError as e:
        logging.exception(f'Ocorreu um erro ao enviar informações a fila sqs. {e}')
        raise Exception(f'Ocorreu um erro ao enviar informações a fila sqs. {e}')
