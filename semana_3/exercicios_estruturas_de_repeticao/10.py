""" Faça um programa que lê três números inteiros e os mostra em ordem
crescente """

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))

maior = medio = menor = 0

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num3 and num2 > num1:
    maior = num2
else:
    maior = num3

if num1 > num2 and num1 < num3:
    medio = num1
elif num2 > num3 and num2 < num1:
    medio = num2
else:
    medio = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    medio = num2
else:
    menor = num3


print(f'A ordem crescente dos números é {menor}, {medio}, {maior}')
