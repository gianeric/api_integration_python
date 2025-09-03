import boto3
import botocore.exceptions
import json 

class OrderSqsPublisher:
    def __init__(self, logger):
        self.logger = logger

    def send(self, payload):
        self.logger.info("[order_sqs_publisher] Iniciando envio para fila SQS pedidos.")
        try:
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
            
            self.logger.info("[order_sqs_publisher] Pedido enviado a fila sqs.", response=response_sqs_send)
            return response_sqs_send
        except botocore.exceptions.ClientError as e:
            self.logger.info("[order_sqs_publisher] Ocorreu um erro ao enviar informações a fila sqs (ClientError).", error=str(e))
            raise
        except botocore.exceptions.EndpointConnectionError as e:
            self.logger.info("[order_sqs_publisher] Não foi possível conectar ao endpoint SQS.", error=str(e))
            raise
        except botocore.exceptions.NoCredentialsError as e:
            self.logger.info("[order_sqs_publisher] Credenciais AWS não encontradas.", error=str(e))
            raise
        except botocore.exceptions.PartialCredentialsError as e:
            self.logger.info("[order_sqs_publisher] Credenciais AWS incompletas.", error=str(e))
            raise
        except Exception as e:
            self.logger.info("[order_sqs_publisher] Ocorreu um erro ao enviar informações a fila sqs.", error=str(e))
            raise
