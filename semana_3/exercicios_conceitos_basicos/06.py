""" Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h """

distancia = float(input('Qual a distância percorrida em km?'))

tempo_aviao = distancia / 600
tempo_carro = distancia / 100
tempo_onibus = distancia / 80

print(f'O tempo de avião seria {tempo_aviao:.2f} horas.')
print(f'O tempo de carro seria {tempo_carro:.2f} horas.')
print(f'O tempo de ônibus seria {tempo_onibus:.2f} horas.')
