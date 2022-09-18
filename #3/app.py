# Herança e Sobreposição

class Pessoa(object):

    def __init__(self, nome, cpf, idade):  # método construtor
        print('teste')  # esse codigo será executado quando instanciamos.
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def exibe_cpf(self):
        print(self.cpf)


class Secretario(Pessoa):
    
    def __init__(self, id_secretario, nome, cpf, idade):
        super().__init__(nome, cpf, idade)  # herda atributos de Pessoa
        self.id_secretario = id_secretario
      # possui método exibe_cpf (herdou de pessoa)

    def exibe_id_secretario(self):
        print(self.id_secretario)

class Vendedor(Pessoa):
    pass


s1 = Secretario("1901", "Vania", 19808091000, 34)
s1.exibe_id_secretario()  # 1901 

v1 = Vendedor("Marcio", 16729819000, 31)
v1.exibe_cpf()
