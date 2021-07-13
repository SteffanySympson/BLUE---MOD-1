# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior, 
# crie um lançador de dados e moedas em que o usuário deve escolher o objeto a ser lançado. 
# Não esqueça que os lançamentos são feitos de forma randômica.

import random

class jogo:
    def __init__(self,item):
        self.item = item

    def lancar_dados(self):
        print(random.randint(1,6))

    def lancar_moeda(self):
        faces_moedas = ['cara','coroa']         
        print(random.choice(faces_moedas))

ask = input('Escolha entre lançamento de DADOS ou MOEDA: ').upper()
if ask == 'DADOS':
    jogo.lancar_dados(ask)
elif ask == 'MOEDA':
    jogo.lancar_moeda(ask)
