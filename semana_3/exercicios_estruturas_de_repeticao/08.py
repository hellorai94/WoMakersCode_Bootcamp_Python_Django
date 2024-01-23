""" . Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado. """


num_1 = int(input("Digite o primeiro número:"))
num_2 = int(input("Digite o segundo número:"))
num_3 = int(input("Digite o terceiro número:"))

if num_1 > num_2 and num_1 > num_3: 
    maior = num_1
elif num_2 > num_1 and num_2 > num_3:
    maior = num_2
else:
    maior = num_3

print(f"O maior número entre {num_1}, {num_2} e {num_3} é {maior}")

