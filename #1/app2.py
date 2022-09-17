from webbrowser import get


class Usuario:

    cargo = 'usuario do sistema'

    def __init__(self, nome, idade, altura):  # método chamado sempre que crio uma instância daquela classe.
        self.x = 1  # significa que a instância tem acesso a esse valor. 
        self.altura = altura
        print(nome, ", ", idade, "anos.")

    def return_altura(self):
        print(self.altura)

    def return_cargo(cls):
        print(cls.cargo)


Usuario.cargo = 'Gerente'  # altera a classe

usuario0 = Usuario("Deonira", 31, 1.71)
usuario0.cargo = "Administrador"
usuario0.x = 10
print(usuario0.x)
usuario0.return_cargo()

usuario1 = Usuario("Maria Luiza", 17, 1.60)
usuario1.return_altura()
usuario1.return_cargo()
print(usuario1.x)




# self referencia a instância, não altera totalmente a classe, apenas a instância.