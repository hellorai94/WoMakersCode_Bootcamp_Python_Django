""" Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais. """

from unidecode import unidecode

frase = (unidecode(input("Digite uma frase:"))).upper()

def contar_vogais(frase):
    vogais = 'AEIOU'
    count = 0  
    for i in frase:
        if i in vogais:
            count += 1
    print(f'O número total de vogais é {count} vogais.')

contar_vogais(frase)
