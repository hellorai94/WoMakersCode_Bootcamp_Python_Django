""" O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
 """

pares = 0
impares = 0

while True:
    numero = int(input("Digite um número:"))

    if numero ==  0:
        break
    elif numero > 0 and numero % 2 == 0:
        pares += 1
    elif numero > 0 and numero % 2 != 0:
        impares += 1
    
print(f'A quantidade de números pares é {pares} e a quantidade de números impares é {impares}.')


