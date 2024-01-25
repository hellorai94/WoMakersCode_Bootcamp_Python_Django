""" Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
 """

peso = float(input("Qual o seu peso (em kg)?"))
altura = float(input("Qual a sua altura (em metros)?"))

imc = peso / (altura ** 2)

print(f"O seu Índice de Massa Corporal (IMC) é: {imc:.2f}.")