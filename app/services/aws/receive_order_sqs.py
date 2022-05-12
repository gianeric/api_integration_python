import boto3
import botocore.exceptions
import json 
import logging


def receive():
    try:
        logging.info('Recebendo pedido da fila sqs...')
        sqs = boto3.client('sqs',
                           region_name='sa-east-1',
                           endpoint_url='http://localhost:4566'
                          )
        
        queue_url = 'http://localhost:4566/000000000000/sqsfilapedido'

        response_sqs_received = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=[],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'All'
            ],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )
        
        logging.info('Pedido recebido da fila sqs.')
        logging.info(response_sqs_received['Messages'][0])
        print(response_sqs_received['Messages'][0])
        return response_sqs_received
        
    except botocore.exceptions.ClientError as e:
        logging.exception(f'Ocorreu um erro ao enviar informações a fila sqs. {e}')
        raise Exception(f'Ocorreu um erro ao enviar informações a fila sqs. {e}')
