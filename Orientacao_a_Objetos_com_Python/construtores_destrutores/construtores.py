""" Um construtor é um método especial que é chamado automaticamente quando uma nova instância de uma classe é criada. O construtor é usado para inicializar o estado da nova instância.

O nome do construtor padrão em Python é __init__(). O construtor pode ter argumentos, que são usados para inicializar os atributos da nova instância. """

# Construtor padrão
class MinhaClasseUm:
    def __init__(self):
        print('MinhaClassUm: Chamou o construtor padrão.')

# Construtor implícito
class MinhaClasseDois:
    pass

# Construtor parametrizado
class MinhaClasseTres:
    def __init__(self, param):
        print(f'MinhaClasseTres: Chamou o construtor parametrizado com o parâmetro {param}.')

objetoUm = MinhaClasseUm()
objetoDois = MinhaClasseDois()
objetoTres = MinhaClasseTres('Dori')


