# Definição da classe Carro
class Carro:
    # O método __init__ é chamado quando um objeto Carro é criado
    def __init__(self, placa):
        # Inicialização de atributos
        self.placa = placa
        # Inicializado como False, para indicar que o carro não está estacionado
        self.estacionado = False

    # Modifica o atributo 'estacionado' do objeto 'Carro'. 
    # Indica que o carro tá estacionado
    def estacionar(self):
        self.estacionado = True

    # Indica que o carro não tá estacionado
    def sair_da_vaga(self):
        self.estacionado = False

class Moto:
    # O método __init__ é chamado quando um objeto Moto é criado
    def __init__(self, placa):
        # Inicialização de atributos
        self.placa = placa
        self.estacionado = False
    
    # Modifica o atributo 'estacionado' do objeto 'Carro'. 
    # Indica que o carro tá estacionado
    def estacionar(self):
        self.estacionado = True

    # Indica que o carro não tá estacionado
    def sair_da_vaga(self):
        self.estacionado = False

        
class Vaga:
    # O método __init__ é chamado quando um objeto Vaga é criado
    def __init__(self, id, tipo):
        # Inicialização de atributos
        self.id = id 
        self.livre = True # A vaga começa como livre
        
        # Verificar se o tipo é carro ou moto, caso não seja, levanta um erro
        if tipo is not 'carro' and tipo is not 'moto':
            raise ValueError(f'O tipo de vaga {tipo} não foi reconhecido')
        
        self.tipo = tipo
        self.placa = None # Inicialmente não há veículo estacionado na vaga

        def ocupar(self, placa):
            if self.livre is False:
                raise ValueError(f'A vaga {self.id} já está ocupada.')
            
            self.placa = placa
            self.livre = False

                




