""" Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês """

valor_hora = float(input("Quantos reais você ganha por hora? "))
horas_mes = float(input('Quantas horas você trabalhou neste mês?'))

salario = valor_hora * horas_mes
print(f'Seu salário foi de {salario:.2f} reais.')