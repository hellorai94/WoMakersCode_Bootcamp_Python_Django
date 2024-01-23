""" Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos. """

num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
num3 = float(input('Digite o terceiro número:'))

def soma(num1, num2, num3):
    soma = num1 + num2 + num3
    print(f'A soma é de {soma}.')

soma(num1, num2, num3)

