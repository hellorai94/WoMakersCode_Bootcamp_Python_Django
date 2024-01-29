""" 
Em Python, um destrutor é um método especial que é chamado automaticamente quando uma instância de uma classe é destruída. O destrutor é usado para liberar recursos alocados pela instância.

O nome do destrutor padrão em Python é __del__(). O destrutor não pode ter argumentos. """

# Construtor padrão

class MinhaClasse:
    def __init__(self, nome):
        self.nome = nome
        print(f'MinhaClasseUm: Chamou o construtor padrão de {nome}.')

    def __del__(self):
        print(f'MinhaClasseUm: Chamou o destrutor de {self.nome}.')

# O momento de execucação de um destrutor é depois que o programa tem seu encerramento solicitado
print('Começou a execucação do programa')
objetoUm = MinhaClasse('objetoUm')
print('Vai terminar a execucação do programa.')
exit()

# Quando todas as referências a um objeto são excluídas, o destrutor é automaticamente chamado  
print('Começou a execucação do programa.')
objetoUm = MinhaClasse('objetoUm')
objetoDois = MinhaClasse('objetoDois')
del objetoUm
print(f'Vai terminar a execucação do programa.')



