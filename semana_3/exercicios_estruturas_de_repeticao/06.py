""" Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro. """

login = 'admin'
senha = 'admin123'

login_user = input('Digite o login:')
senha_user = input('Digite a senha:')

if login_user == login and senha_user == senha:
    print('Credencias corretas!')
else:
    print('Login ou senha errados!')
    