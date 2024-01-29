class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self._tipo = 'Pessoa'

    def falar_oi(self):
        print(f'Oi! Meu nome é {self._nome}.')
    
    def falar_tipo(self):
        print(f'O meu tipo é {self._tipo}.')

pessoa = Pessoa('Raissa')
pessoa.falar_oi()
pessoa.falar_tipo()
print()


# Classe derivada - Estudante é uma pessoa
class Estudante(Pessoa):
    def __init__(self, nome, curso):
        # Chama o construtor da classe base
        super().__init__(nome) 
        self._curso = curso

    def falar_curso(self):
        # self._nome é herdada da classe base
        print(f'Eu, {self._nome}, estudo o curso "{self._curso}".')

    # Sobrescrever a função original da classe base
    def falar_tipo(self):
        self._tipo = 'Estudante'
        return super().falar_tipo()
    
estudante = Estudante('Raissa', 'Introdução a Python')
# O método é herdado da classe base
estudante.falar_oi()
# Herdado mas sobrescrito
estudante.falar_tipo()
estudante.falar_curso()
print()

# Determinar se um objeto é de um determinado tipo em tempo de execucação com as funções:
print('O objeto estudante é uma instância da classe Estudante?', isinstance(estudante, Estudante))
print('O objeto estudante é uma instância da classe Pessoa?', isinstance(estudante, Pessoa))
print('A classe Estudante é uma sub-classe de Pessoa?', issubclass(Estudante, Pessoa))
print('A classe Pessoa é uma sub-classe da classe Estudante?', isinstance(Pessoa, Estudante))

# Herança transitiva - A classe Trabalhador herda de Pessoa que pode sua vez será herdada da classe Professor

class Trabalhador(Pessoa):
    def __init__(self, nome, profissao):
        # Chama o construtor da classe base
        super().__init__(nome) 
        # Atributo privado - Só pode ser acessado dentro da classe Trabalhador
        self.__profissao = profissao 
        self._tipo = 'Trabalhador'

    def falar_profissao(self):
        print(f'Eu, {self._nome}, exerço a profissão "{self.__profissao}".')

    # Sobrescreve a função original da classe Pessoa
    def falar_tipo(self): 
        return super().falar_tipo()

trabalhadora = Trabalhador('Raissa', 'Proletária')
trabalhadora.falar_oi()
trabalhadora.falar_tipo()
trabalhadora.falar_profissao()
print()


class Professor(Trabalhador):
    def __init__(self, nome, disciplina):
        super().__init__(nome, 'Professor')
        self.__disciplina = disciplina

    def falar_profissao(self):
        # Variáveis privadas não conseguem ser alteradas pela classe derivada
        self.__profissao = 'Instrutora'
        return super().falar_profissao()
    
    def falar_disciplina(self):
        print(f'Eu, {self._nome}, dou aulas da disciplina" {self.__disciplina}"')

    def falar_tipo(self): 
        # Sobrescreve a função original da classe Pessoa
        self._tipo = 'Professor'
        return super().falar_tipo()
    
professora = Professor('Raissa', 'Python')
professora.falar_oi()
professora.falar_profissao()
professora.falar_tipo()
professora.falar_disciplina()
print()

# Todas classes herdam implicitamente da classe object
class Humano:
    pass

# Humano já inicializa com vários atributos e métodos
humano = Humano()
print(dir(humano))
print()

# Os atributos e métodos inicializadas também vem nas classes que criamos, além dos atributos e métodos criados por nós

print(dir(Trabalhador))
print()