class Usuario:

    cargo = 'usuario do sistema'

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def entrar_no_sistema(self):
        print(f"Entrando no sistema como {self.nome}")

    def retornar_cargo(self):
        print(self.cargo)

    def retornar_idade(self):
        print(self.idade)



usuario0 = Usuario("Luana", 21, 1.57)
usuario0.cargo = "Gerente"
print(usuario0.cargo)
usuario0.retornar_idade()
usuario0.entrar_no_sistema()


usuario1 = Usuario("Leandro", 24, 1.92)
usuario1.retornar_cargo()
usuario1.retornar_idade()
