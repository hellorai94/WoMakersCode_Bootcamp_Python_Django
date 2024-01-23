""" Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.
 """
horas_semana = float(input('Quantas horas de exercício físico você fez?'))

calorias = ((horas_semana * 4) * (5 * 60))
print(f'A quantidade de calorias queimadas em um mês foi de {calorias} calorias.')

