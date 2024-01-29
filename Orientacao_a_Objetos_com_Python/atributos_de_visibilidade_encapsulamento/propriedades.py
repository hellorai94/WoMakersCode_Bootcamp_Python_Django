""" Em Python, propriedades são um recurso que permitem acessar e modificar atributos de uma classe de forma mais elegante e segura.

Ao usar propriedades, você pode evitar o acesso direto aos atributos de uma classe, o que pode levar a erros. Você também pode usar propriedades para validar os valores que são atribuídos aos atributos. """

class Quadrado:
    def __init__(self, medida):
        self.altura = medida
        self.largura = medida

    # O decorador @property indica que o método a seguir é uma propriedade
    @property
    # Define a propriedade altura
    def altura(self):
        print('getter de altura')
        return self.__medida
       
    # O decorador @altura.setter indica que o método a seguir é o setter da propriedade altura.
    @altura.setter
    def altura(self, valor):
        print('setter de altura')
        if valor < 0:
            raise ValueError()
            self.__medida = valor
 
    @property
    def largura(self):
        print('getter de largura')
        return self.__medida
    
    @largura.setter
    def largura(self, valor):
        print('setter de largura')
        if valor < 0:
            raise ValueError()
        self.__medida = valor

    def area(self):
        return self.largura * self.altura

quadrado = Quadrado(2)
quadrado.largura = 3
print(quadrado.area())