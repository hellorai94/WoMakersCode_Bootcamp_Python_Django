""" Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área. """

nome = input("Qual o seu nome?")
idade = input("Qual a sua idade?")
cidade = input("De qual cidade você é?")
palavra = input("Qual sua palavra preferida?")

print(f'Olá, {nome}. Espero que esteja bem.')
print(f'Que legal que você tem {idade} anos. Toda idade tem o seu valor e o tempo não é linear. Tentar é possível.')
print(f'O que tem de bom para fazer em {cidade}?')
print(f'{palavra} é importante.')
