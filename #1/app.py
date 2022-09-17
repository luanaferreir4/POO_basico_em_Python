class Usuario:
    cargo = 'usuario'  # atributo (variável dentro da classe) de todos os usuários.

    def log_in(self):  #  ação
        print('Logado!')

    def log_out(self):
        print('Saindo!')


usuario1 = Usuario()
print(usuario1)
print(usuario1.cargo)
usuario1.log_in()
usuario1.log_out()

usuario2 = Usuario()
usuario2.log_in()
usuario2.log_out()
# atributos = valores da determinada classe.

# métodos = o que aquela determinada classe faz (objeto) - função dentro de uma classe.

