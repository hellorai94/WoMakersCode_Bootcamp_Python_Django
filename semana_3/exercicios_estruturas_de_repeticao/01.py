""" Faça um Programa que peça dois números e imprima o maior deles. """

num_1 = float(input("Digite o primeiro número:"))
num_2 = float(input("Digite o segundo número:"))

if num_1 > num_2:
    print(f'O maior número entre {num_1} e {num_2} é {num_1}.')
elif num_2 > num_1:
    print(f'O maior número entre {num_1} e {num_2} é {num_2}.')
else:
    print(f'O número {num_1} e o número {num_2} são iguais.')
    

