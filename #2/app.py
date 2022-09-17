# Métodos de classe x Métodos estáticos

class Usuario:

    cargo = 'usuario'

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def retorna_altura(self):
        print(self.altura)

    @classmethod  # afirma que não é mais um método de instancia, agora posso acessar esse método diretamente pela classe, o self é o simbolo de instancia, cls é o simbolo de estatico.
    def retorna_cargo(cls):
        cls.cargo = 'Gerente'
        print(cls.cargo)

user0 = Usuario("Luana", 21, 1.60)
user0.retorna_altura()

Usuario.retorna_cargo()


# ------------------------------------------------------------------------------------------------


class Usuario:

    cargo = 'usuario'

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def retorna_altura(self):
        print(self.altura)

    @staticmethod  # método auxiliar (quando não precisar saber atributos de classe e nem precisar chamar uma função de instância (atributos).)
    def eh_adulto(idade):
        if idade > 17:
            print("Sim, é adulto!")
        else:
            print("Não é adulto!")
    


Usuario.eh_adulto(18)