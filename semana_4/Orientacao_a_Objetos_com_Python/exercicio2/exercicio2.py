from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self._telefone = telefone
        self.__renda_mensal = renda_mensal

    