import sqlite3

conexao = sqlite3.connect('banco_teste')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')
#cursor.execute('DROP TABLE produtos')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (1, "Rihanna", "Salvador", "riri@gmail.com", 123455)')
#cursor.execute('DELETE FROM usuario WHERE id = 1')
""" cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (2, "Beyonce", "Houston", "beyonce@gmail.com", 678910)')
cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (3, "Ariana Grande", "Boca Raton", "arianagrande@gmail.com", 234567)')
cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (4, "Shakira", "Columbia", "shakira@gmail.com", 987654)')
 """
""" dados = cursor.execute('SELECT * FROM usuario ')
for i in dados:
    print(i)

cursor.execute('UPDATE usuario SET endereco = "Minas Gerais" WHERE nome = "Ariana Grande"')  """
# ORDER BY E DESC
""" dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')
for i in dados:
    print(i) """
# LIMIT E DISTINCT
""" dados = cursor.execute('SELECT * FROM usuario LIMIT 1')
for i in dados:
    print(i) """

#GROUP BY E HAVING
""" dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id > 3')
for i in dados:
    print(i) """

# JOIN - Right - Left - Full - Inner
""" cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100))') """
cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES (2, "BEBEL", "Mexico", "deus@gmail.com")')

dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')
for usuario in dados:
    print(usuario)
conexao.commit()
conexao.close()
