""" Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
 """

sal_bruto = float(input('Qual o salário bruto?'))

if sal_bruto <= 1903.98:
    print(f'O salário liquído é R$ {sal_bruto:.2f}.')
elif sal_bruto <=  2826.65:
    sal_liq = sal_bruto * 0.925
    print(f'O salário liquído é R$ {sal_liq:.2f}.')
elif sal_bruto <=  3751.05:
    sal_liq = sal_bruto * 0.85
    print(f'O salário liquído é R$ {sal_liq:.2f}.')    
elif sal_bruto <=  4664.68:
    sal_liq = sal_bruto * 0.775
    print(f'O salário liquído é R$ {sal_liq:.2f}.')   
else:
    sal_liq = sal_bruto * 0.725
    print(f'O salário liquído é R$ {sal_liq:.2f}.')   


