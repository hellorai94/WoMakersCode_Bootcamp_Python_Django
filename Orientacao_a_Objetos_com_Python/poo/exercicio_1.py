""" Exercícios Classes e Objetos
1. Crie uma classe que modele o objeto "carro".
2. Um carro tem os seguintes atributos: ligado, cor, modelo,
velocidade.
3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,
desacelera.
4. Crie uma instância da classe carro.
5. Faça o carro "andar" utilizando os métodos da sua classe.
6. Faça o carro "parar" utilizando os métodos da sua classe """


# Definindo a classe Carro (1. Crie uma classe que modele o objeto "carro".)
class Carro:
    # O método __init__ é o construtor da classe, usado para inicializar os atributos do objeto
    def __init__(self, cor, modelo, ligado=False, velocidade=0):
        # 2. Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
        self.cor = cor          # Atributo que armazena a cor do carro
        self.modelo = modelo    # Atributo que armazena o modelo do carro
        self.ligado = ligado    # Atributo que indica se o carro está ligado ou não (inicializado como False)
        self.velocidade = velocidade  # Atributo que armazena a velocidade do carro (inicializado como 0)

    # 3. Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
    # Método para ligar o carro
    def liga(self):
        if not self.ligado:
            print(f'O carro {self.modelo} está ligado.')
            self.ligado = True
        else:
            print(f'O carro {self.modelo} já está ligado.')

    # Método para desligar o carro
    def desliga(self):
        if self.ligado:
            print(f'O carro {self.modelo} está desligado.')
            self.ligado = False
            self.velocidade = 0
        else:
            print(f'O carro {self.modelo} está desligado.')

    # Método para acelerar o carro
    def acelera(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade
            print(f'O carro {self.modelo} está acelerando a {self.velocidade}')
        else:
            print(f'O carro {self.modelo} precisa estar ligado para acelerar.')

# 4. Crie uma instância da classe carro.
# Criando uma instância da classe Carro
carro = Carro(cor='Amarelo', modelo='Fusca')

# 5. Faça o carro "andar" utilizando os métodos da sua classe.
# 6. Faça o carro "parar" utilizando os métodos da sua classe """
# Chamando métodos para ligar, acelerar e desligar o carro
carro.liga()  # Ligar o carro
carro.acelera(25)  # Acelerar o carro em 25 unidades
carro.acelera(50)  # Acelerar o carro em mais 50 unidades
carro.desliga()  # Desligar o carro
