""" Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l. """

litros = float(input("Qual a quantidade de litros de combustível consumidos?"))
distancia = float(input("Qual foi a distância percorrida?"))

consumo = distancia / litros
print(f'O consumo médio foi de {consumo:.2f} km/l.')


