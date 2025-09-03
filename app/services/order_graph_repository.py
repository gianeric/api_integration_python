from models.aws.order import Order
from models.aws.person import Person
from models.aws.address import Address
from models.aws.order_itens import OrderItens

class OrderGraphRepository:
    def __init__(self, logger):
        self.logger = logger

    def save_order_graph(self, payload):
        self.logger.info("[order_graph_repository] Iniciando salvamento no banco grafo.")
        try:
            self.import_order()
            self.import_person()
            self.import_address()
            self.import_order_itens()
            self.logger.info("[order_graph_repository] Dados salvos com sucesso no banco grafo.")
        except Exception as e:
            self.logger.info("[order_graph_repository] Ocorreu um erro ao salvar dados no banco grafo.", error=str(e))
            raise Exception(f'Ocorreu um erro ao salvar dados no banco grafo. {e}')
    
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

