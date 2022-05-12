from models.aws.order import Order
from models.aws.person import Person
from models.aws.address import Address
from models.aws.order_itens import OrderItens
import logging


class OrderGraph():
    def __init__(self):
        self.import_order()

    def import_order(self):
        order = Order()
        order.codigo_pedido = "Credito"
        order.codigo_pedido = codigo_pedido
        order.data_pedido = data_pedido
        order.nome_pedido = nome_pedido
        order.tipo_pedido = tipo_pedido
        order.dados_pessoa = dados_pessoa
        order.itens_pedido = itens_pedido

    def import_person(self):
        person = Person()
        person.nome = nome
        person.data_nascimento = data_nascimento
        person.endereco = endereco

    def import_address(self):
        address = Address()
        address.descricao = descricao
        address.lougradouro = lougradouro
        address.bairro = bairro
        address.cidade = cidade
        address.cep = cep

    def import_order_itens(self):
        order_itens = OrderItens()
        order_itens.descricao = descricao

    def save(payload):
        logging.info('Salvando dados no banco grafo.')
