""" Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.
 """

cont = 0
lista_media = []

while cont < 5:
    print("=============================================")
    nota_um = float(input("Qual a sua primeira nota?"))
    nota_dois = float(input("Qual a sua segunda nota?"))
    nota_tres = float(input("Qual a sua terceira nota?"))
    nota_quatro = float(input("Qual a sua quarta nota?"))
    media = (nota_um + nota_dois + nota_tres + nota_quatro) / 4
    lista_media.append(media)
    print(f'A média é: {media}.')
    cont +=1

cont_list = 0
for i in lista_media:
    print(i)
    if i >= 7:
        cont_list +=1

print(f'A quantidade de alunos com média maior ou igual a 7.0 é {cont_list}')
    



