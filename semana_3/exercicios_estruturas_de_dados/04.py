""" Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome. """

nome = input("Você quer o contato de quem?").upper()

agenda = {
    'RAISSA': '7592989894',
    'JUCI': '7598662145',
    'HELLEN': '7589644220',
    'JOAO': '123456789',
    'MARIA': '987654321',
    'CARLOS': '555555555',
    'ANA': '999999999'
}

if nome in agenda:
    print(agenda[nome])
else:
    print(f'O nome {nome} não está na lista.')

        


                 
