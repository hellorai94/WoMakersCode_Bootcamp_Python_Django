import sqlite3
import random
conexao = sqlite3.connect('banco_dois')
cursor = conexao.cursor()

# Questão 5
#cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT(20))')

""" for i in range(1, 51):
    nome = f'Cliente{i}'
    idade = random.randint(18, 60)
    saldo = round(random.uniform(1000, 50000), 2)
    
    cursor.execute('INSERT INTO clientes VALUES (?, ?, ?, ?)', (i, nome, idade, saldo))
 """

# Questão 6
""" dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
for i in dados:
    print(i) """
    
""" media = cursor.execute('SELECT AVG(saldo) FROM clientes')
media = cursor.fetchone()
print(media) """

""" max_saldo = cursor.execute('SELECT MAX(saldo) FROM clientes')
max_saldo = cursor.fetchone()
print(max_saldo) 
 """

""" dados = cursor.execute('SELECT COUNT(nome) FROM clientes WHERE saldo > 1000')
dados = cursor.fetchone()
print(dados)  """

# Questão 7
#cursor.execute('UPDATE clientes SET saldo = 0 WHERE id = 7')   
#cursor.execute('DELETE FROM clientes WHERE id = 22')  

# Questão 8 
#cursor.execute('CREATE TABLE compras(id INT, cliente_id INT, produto VARCHAR(100), valor REAL(20))')
""" 
for compra_id in range(1, 101):
    cliente_id = random.randint(1, 50)
    produto = f'Produto{compra_id}'
    valor = round(random.uniform(10, 200), 2)
    
    cursor.execute('INSERT INTO compras VALUES (?, ?, ?, ?)', (compra_id, cliente_id, produto, valor)) """

dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id=compras.cliente_id')
for i in dados:
    print(i)

conexao.commit()
conexao.close()
