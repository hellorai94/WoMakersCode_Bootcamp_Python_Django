class Pessoa:
    def __init__(self, nome, signo, identidade):
        # Protegida
        self._nome = nome
        self.signo = signo
        # Atributo Privado - Não pode ser alterado
        self.__identidade = identidade

    def __str__(self):
        return f'Nome: {self._nome}, Signo: {self.signo}, Identidade: {self.__identidade}.'

    
pessoaUm = Pessoa('Raissa', 'Touro',  '4459632452')
print(pessoaUm)
print()

pessoaUm.signo = 'Aquario'
print(pessoaUm)
print()

pessoaUm.__identidade = '12344'
print(pessoaUm)
print()


