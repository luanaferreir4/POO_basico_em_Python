# Pergunta/Tarefa:

# Crie uma classe para representar uma pessoa, com os atributos privados de nome, data de nascimento e altura.
# Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos dados de uma pessoa.
# Crie um método para calcular a idade da pessoa.

# A data de nascimento pode ser informada como uma String (no formato 05/10/1982, por exemplo) e, no cálculo da idade,
# considere apenas o ano da data de nascimento informada.

# Sua saída deverá ser parecida com:

# Nome: Amanda Rodrigues
# Data de Nascimento: 21/05/2001
# Altura: 1.57
# A pessoa tem 21 anos

class Pessoa(object):

    def __init__(self, nome, data_de_nascimento, altura, ano_de_nascimento):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.altura = altura
        self.ano_de_nascimento = ano_de_nascimento

    def get_nome(self):
        print(self.nome)

    def get_data_de_nascimento(self):
        print(self.data_de_nascimento)

    def get_altura(self):
        print(self.altura)

    def print_dados(self):
        print(f" Nome: {self.nome}\nData de Nascimento: {self.data_de_nascimento}\nAltura: {self.altura}\nAno de Nascimento: {self.ano_de_nascimento}")

    def calcula_idade(self):
        ano_atual = 2022
        print(f"A pessoa tem {ano_atual - self.ano_de_nascimento} anos.")
        


p1 = Pessoa("Luana", "21/05/2001", 1.57, 2001)
p1.print_dados()
p1.calcula_idade()

