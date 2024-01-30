import sqlite3

conexao = sqlite3.connect('exercicio')
cursor = conexao.cursor()

# Questão 1
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(50))')

# Questão 2
""" alunos_data = [
    (1, 'João', 20, 'Engenharia'),
    (2, 'Maria', 22, 'Ciência da Computação'),
    (3, 'Carlos', 19, 'Administração'),
    (4, 'Ana', 21, 'Medicina'),
    (5, 'Pedro', 23, 'Economia'),
    (6, 'Julia', 20, 'Arquitetura'),
    (7, 'Lucas', 22, 'Psicologia'),
    (8, 'Camila', 21, 'Direito'),
    (9, 'Gabriel', 20, 'Design'),
    (10, 'Isabela', 23, 'Biologia')
]

for aluno in alunos_data:
    cursor.execute('INSERT INTO alunos VALUES (?, ?, ?, ?)', aluno)
 """

# Questão 3
""" dados = cursor.execute('SELECT * FROM alunos')
for i in dados:
    print(i) """

""" dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for i in dados:
    print(i)
     """
""" alunos_engenharia = [
    (11, 'João', 20, 'Engenharia'),
    (12, 'Mariana', 22, 'Engenharia'),
    (13, 'Lucas', 19, 'Engenharia'),
    (14, 'Beatriz', 21, 'Engenharia'),
    (15, 'Rafael', 23, 'Engenharia')
]

for aluno in alunos_engenharia:
    cursor.execute('INSERT INTO alunos VALUES (?, ?, ?, ?)', aluno) """

""" dados = cursor.execute('SELECT nome FROM alunos WHERE curso == "Engenharia" ORDER BY nome ASC')
for i in dados:
    print(i)
 """

""" dados = cursor.execute('SELECT COUNT(nome) FROM alunos')
dados = cursor.fetchone()
print(dados) """

# Questão 4

""" cursor.execute('UPDATE alunos SET idade = 64 WHERE nome = "Lucas"')   """
cursor.execute('DELETE FROM alunos WHERE id = 7')

conexao.commit()
conexao.close()


