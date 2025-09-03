import boto3
import botocore.exceptions

class OrderSqsReceiver:
    def __init__(self, logger):
        self.logger = logger

    def receive(self):
        self.logger.info("[order_sqs_receiver] Iniciando recebimento da fila SQS pedidos.")
        try:
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
            
            self.logger.info("[order_sqs_receiver] Pedido recebido da fila sqs.", response=response_sqs_received)
            return response_sqs_received
        except botocore.exceptions.ClientError as e:
            self.logger.info("[order_sqs_receiver] Ocorreu um erro ao receber informações a fila sqs (ClientError).", error=str(e))
            raise
        except botocore.exceptions.EndpointConnectionError as e:
            self.logger.info("[order_sqs_receiver] Não foi possível conectar ao endpoint SQS.", error=str(e))
            raise
        except botocore.exceptions.NoCredentialsError as e:
            self.logger.info("[order_sqs_receiver] Credenciais AWS não encontradas.", error=str(e))
            raise
        except botocore.exceptions.PartialCredentialsError as e:
            self.logger.info("[order_sqs_receiver] Credenciais AWS incompletas.", error=str(e))
            raise
        except Exception as e:
            self.logger.info("[order_sqs_receiver] Ocorreu um erro ao receber informações a fila sqs.", error=str(e))
            raise
