'''Modelagem de um estacionamento'''

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
        if tipo != 'carro' and tipo != 'moto':
            raise ValueError(f'O tipo de vaga {tipo} não foi reconhecido')
        
        self.tipo = tipo
        self.placa = None # Inicialmente não há veículo estacionado na vaga

    def ocupar(self, placa):
        if self.livre is False:
            raise ValueError(f'A vaga {self.id} já está ocupada.')
        
        self.placa = placa
        self.livre = False

    def desocupar(self, placa):
        if self.livre is True:
            raise ValueError(f'A vaga {self.id} já está lvire.')
            
class Estacionamento:
    def __init__(self, total_vagas_livres_carro, total_vagas_livres_motos):
        self.carro_para_vaga = {}
        self.moto_para_vaga = {}
        self.total_vagas_livres_carro = total_vagas_livres_carro
        self.total_vagas_livres_moto = total_vagas_livres_motos
        # Chama o método inicializar_vagas() da instância
        self.inicializar_vagas()

    def inicializar_vagas(self):
        self.vagas_carro = {}
        self.vagas_moto = {}

        tipo = 'carro'
        for i in range(self.total_vagas_livres_carro): 
            # Cria uma nova instância da classe Vaga e a instância é adicionada ao dicionário usando o índice i como chave
            self.vagas_carro[i] = Vaga(i, tipo)

        # O primeiro id de motos será o total de vagas livros de carro - Pq a interação que vai ocorrer em tipo 'carro' é -1 então.
        primeiro_id_motos = self.total_vagas_livres_carro 
        # O último será o primeiro id de motos + o total de vagas livres
        ultimo_id_motos = primeiro_id_motos + self.total_vagas_livres_carro
        tipo = 'moto'
        # Cria uma nova instância da classe Vaga e a instância é adicionada ao dicionário usando o índice i como chave
        for j in range(primeiro_id_motos, ultimo_id_motos):
            self.vagas_moto[j] = Vaga(j, tipo)

    # O valor do parametro do método é uma instância da classe carro.
    def estacionar_carro(self, carro: Carro):
        if carro.estacionado is True:
            raise ValueError(f'O carro {carro.placa} já está no estacionamento.')

        # Atribui os valores retornados pelo método buscar_id_da_proxima_vaga_livre() as variáveis id_da_proxima_vaga e tipo 
        id_da_proxima_vaga, tipo = self.buscar_id_da_proxima_vaga_livre('carro')
        if id_da_proxima_vaga is None:
            raise ValueError(f'Não há mais vagas de carro disponíveis no estacionamento.')
        elif id_da_proxima_vaga != None and tipo is 'carro':
            # 
            vaga = self.vagas_carro[id_da_proxima_vaga]
            # Marca a vaga como ocupada atribuindo a placa do carro à vaga
            vaga.ocupar(carro.placa)
            # Chama o método estacionar() da instância carro, atualizando seu estado para estacionado.
            carro.estacionar()
            # Associa a placa do carro ao número da vaga ocupada
            self.carro_para_vaga[carro.placa] = vaga.id
            # Decrementao número de vagas livres
            self.total_vagas_livres_carro -= 1
        else:
            # 
            raise RuntimeError(f'Erro interno - não foi possível recuperar a próxima vaga de carro.')
        
        print(f'Carro {carro.placa} estacionado na vaga {vaga.id} do tipo {vaga.tipo}')


    def estacionar_moto(self, moto: Moto):
        if moto.estacionado is True:
            raise ValueError(f'O carro {moto.placa} já está no estacionamento.')
        id_da_proxima_vaga, tipo = self.buscar_id_da_proxima_vaga_livre('moto')

        if id_da_proxima_vaga is None:
            raise ValueError(f'Não há mais vagas de moto disponíveis no estacionamento.')
        elif id_da_proxima_vaga != None and tipo is 'moto':
            vaga = self.vagas_moto[id_da_proxima_vaga]
            vaga.ocupar(moto.placa)
            moto.estacionar()
            self.moto_para_vaga[moto.placa] = vaga.id
            self.total_vagas_livres_moto -= 1
        elif id_da_proxima_vaga != None and tipo is 'carro':
            vaga = self.vagas_carro[id_da_proxima_vaga]
            vaga.ocupar(moto.placa)
            moto.estacionar()
            self.moto_para_vaga[moto.placa] = vaga.id
            self.total_vagas_livres_carro -= 1
        else:
            raise RuntimeError(f'Erro interno - não foi possível recuperar a próxima vaga de moto.')
        
        print(f'Moto {moto.placa} estacionada na vaga {vaga.id} do tipo {vaga.tipo}.')

    def buscar_id_da_proxima_vaga_livre(self, tipo):
        if tipo == 'carro':
            if self.total_vagas_livres_carro > 0:
                # Itera sobre as chaves do dicionário self.vagas_carro
                for identificador in self.vagas_carro.keys():
                    vaga = self.vagas_carro[identificador]
                    if vaga.livre is True:
                        return identificador, 'carro'
            else:
                # Não acha vaga de carro
                # Retorna o valor None e a string vazia
                return None, ''
        elif tipo == 'moto':
            if self.total_vagas_livres_moto > 0:
                for identificador in self.vagas_moto.keys():
                    vaga = self.vagas_moto[identificador]
                    if vaga.livre is True:
                        return identificador, 'moto'
            if self.total_vagas_livres_carro > 0:
                for identificador in self.vagas_carro.keys():
                    vaga = self.vagas_carro[identificador]
                    if vaga.livre is True:
                        return identificador, 'carro'

            return None, ''
        else:
            raise TypeError(f'Tipo {tipo} não reconhecido.')
        
    def remover_carro(self, carro: Carro):
        # Obtém o identificador da vaga ocupada pelo carro
        id_vaga = self.carro_para_vaga[carro.placa]
        # Obtém a vaga ocupada pelo carro
        vaga = self.vagas_carro[id_vaga]
        # Marca a vaga como desocupada
        vaga.desocupar()
        # Marca o carro como desocupado
        carro.sair_da_vaga()
        # Deleta a associação entre o id e a placa do carro 
        del self.carro_para_vaga[carro.placa]
        # Incrementa o valor de vagas livres para carros
        self.total_vagas_livres_carro += 1
        print(f'Carro {carro.placa} retirado da vaga {vaga.id}')
        return True
    
    def remover_moto(self, moto: Moto):
        id_vaga = self.moto_para_vaga[moto.placa]
        vaga = None

        if id_vaga in self.vagas_moto:
            vaga = self.vagas_moto[id_vaga]
        elif id_vaga in self.vagas_carro:
            vaga = self.vagas_carro[id_vaga]
        else:
            raise ValueError(f'Não foi possível encontrar a vaga com o identificador {id_vaga}')
        
        moto.sair_da_vaga()
        vaga.desocupar()
        del self.moto_para_vaga[moto.placa]
        if vaga.tipo == 'moto':
            self.total_vagas_livres_moto += 1
        else:
            self.total_vagas_livres_carro += 1

        print(f'Moto {moto.placa} retirada da vaga {vaga.id} (tipo {vaga.tipo})')

    def estado_do_estacionamento(self):
        # Obtém a quantidade de carros e motos estacionados
        num_carros_estacionados = len(self.carro_para_vaga)
        num_motos_estacionadas = len(self.moto_para_vaga)
        # Printa a quantidade de carros e motos estacionados e de vagas livres
        estado = ' ----  Estado do Estacionamento ----\n'
        estado += f' Num carros estacionados: {num_carros_estacionados}\n'
        estado += f' Num motos estacionadas: {num_motos_estacionadas}\n'
        estado += f' Total de vagas livres de carros: {self.total_vagas_livres_carro}\n'
        estado += f' Total de vagas livres de motos: {self.total_vagas_livres_moto}\n'
        estado += f' Vagas de carros:\n'
        # Associa o id as placas
        for i in range(len(self.vagas_carro)):
            placa = self.vagas_carro[i].placa
            estado += f'vaga[{i}]: {placa}; '
        estado += f'\n Vagas de motos:\n    '
        id_primeira_vaga_moto = len(self.vagas_carro)
        id_ultima_vaga_moto = id_primeira_vaga_moto + len(self.vagas_moto)
        for i in range(id_primeira_vaga_moto, id_ultima_vaga_moto):
            placa = self.vagas_moto[i].placa
            estado += f'vaga[{i}]: {placa};'
        estado += '\n--------------------------------\n'
        return estado
    
    def __str__(self):
        return self.estado_do_estacionamento()


            
            

                
                    




            








            
                




