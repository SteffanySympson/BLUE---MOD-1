from asciis import Asciis

class Personagem:
    def __init__(self, sexo, nome):
        self.sexo = sexo
        self.nome = nome

    @property
    def nome (self):
        return self.__nome

    @nome.setter
    def nome (self, nomeuser):
        raise ValueError ('Não é possível modificar o nome de usuário antes de um novo jogo.')

    def personagem (self, nome, sexo, cor_olhos, cor_cabelo, contador):
        self.__nome = nome
        self.sexo = sexo
        self.cor_olhos = cor_olhos
        self.cor_cabelo = cor_cabelo
        import time
        print()
        nome = input('Qual será o nome? ').title()
        print(f'Olá {nome}!!!')
        print()
        print('Escolha o sexo do personagem: ')
        print('[1] Feminino\n[2] Masculino')
        print()
        sexo = input('Digite sua opção: ')
        while sexo not in ['1','2']:
            print('Opção inválida!')
            sexo = input('Digite sua opção: ')
        print()
        dic_cor_olhos = {'1':'pretos','2':'azuis','3':'cinza','4':'verdes','5':'violeta'}
        for c,v in dic_cor_olhos.items():
            print(f'[{c}] {v}')
        cor_olhos = input("Escolha a cor dos olhos: ")
        while cor_olhos not in ['1','2','3','4','5']:
            print('Opção inválida!')
            cor_olhos = input("Escolha a cor dos olhos: ")
        if cor_olhos == '1':
            contador.incrementar(2)
        elif cor_olhos == '2':
            contador.incrementar(5)   
        elif cor_olhos == '3':
            contador.incrementar(8)
        elif cor_olhos == '4':
            contador.incrementar(12)
        elif cor_olhos == '5':
            contador.incrementar(10)
        print()
        print(f'Você possui {contador.valor} moedas. Quando chegar a 1.000 Você terá o bastante para voltar para casa!')
        print()
        dic_cor_cabelo = {'1':'verdes','2':'loiros','3':'pretos','4':'prateados','5':'vermelhos','6':'castanhos'}
        for c,v in dic_cor_cabelo.items():
            print(f'[{c}] {v}')
        cor_cabelo = input("Escolha a cor dos cabelos: ")
        while cor_cabelo not in ['1','2','3','4','5','6']:
            print('Opção inválida')
            cor_cabelo = input("Escolha a cor dos cabelos: ")
        if cor_cabelo == '1':
            contador.incrementar(12)
        elif cor_cabelo == '2':
            contador.incrementar(5)
        elif cor_cabelo == '3':
            contador.incrementar(2)
        elif cor_cabelo == '4':
            contador.incrementar(10)
        elif cor_cabelo == '5':
            contador.incrementar(8)
        elif cor_cabelo == '6':
            contador.incrementar(6)
        print()
        print(f'Você possui {contador.valor} moedas.')
        print()           
        if sexo == '1':
            Asciis.Fem()
            print()
            descricao = (f'{nome} é forte, curiosa e determinada. Com lindos cabelos {dic_cor_cabelo[cor_cabelo]} e olhos {dic_cor_olhos[cor_olhos]}, pode parecer frágil e indefesa, mas não se iluda com as aparências...\n¯\_(ツ)_/¯\n')
            for ch in descricao:
                time.sleep(0.1) 
                print(ch, end='', flush=True)
        elif sexo == '2':
            Asciis.Masc()
            print()
            descricao = (f'{nome} é forte, curioso e determinado. Alto, com cabelos {dic_cor_cabelo[cor_cabelo]} e olhos {dic_cor_olhos[cor_olhos]}, um perfeito héroi... (っ▀¯▀)つ\n')
            for ch in descricao:
                time.sleep(0.1)
                print(ch, end='', flush=True)
        print()