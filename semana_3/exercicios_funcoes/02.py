""" Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.
 """

numero = str(int(input("Digite um número:")))

def reverso(numero):
    reverso = numero[::-1]
    print(f'O reverso de {numero} é {reverso}.')

reverso(numero)
