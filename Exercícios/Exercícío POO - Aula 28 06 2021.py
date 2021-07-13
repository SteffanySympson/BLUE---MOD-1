# 1.a) Crie uma classe pessoa com os seguintes atributos: nome,
# sobrenome e idade.
# 1.b) Acrescente a classe criada um método para mostrar os dados de
# uma pessoa.
# 1.c) Crie um objeto do tipo pessoa para testar suas propriedades e
# métodos.

class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def dados(self):
        print(f'Nome completo: {self.nome} {self.sobrenome} ')
        print(f'Idade {self.idade} anos.')

humano = Pessoa("Steffany", "Sympson", 31)
humano.dados()

########

