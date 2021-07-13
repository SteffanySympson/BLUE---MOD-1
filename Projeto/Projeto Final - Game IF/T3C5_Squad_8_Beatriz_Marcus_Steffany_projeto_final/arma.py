from asciis import Asciis

class Arma:
    def escolha_arma(self, escolha_arma, contador):
        import time
        print()
        print("Escolha uma arma para a sua aventura: ")
        dic_arma = {'1':'Espingarda','2':'Arco e Flecha','3':'Espada','4':'Sabre de Luz','5':'Foice','6':'Tridente de Poseidon'}
        for c,v in dic_arma.items():
            print(f'[{c}] {v}')
        escolha_arma = input("Digite a sua opção: ")
        while escolha_arma not in ['1','2','3','4','5','6']:
            print('Opção inválida!')
            escolha_arma = input("Digite a sua opção: ")
        if escolha_arma == "1":
            contador.incrementar(5)
            print()
            espingarda = ("Você escolheu ESPINGARDA. Esperamos que saiba atirar... ")
            for ch in espingarda:
                time.sleep(0.1) 
                print(ch, end='', flush=True)
        elif escolha_arma == "2":
            contador.incrementar(15)
            print()
            arco = ("Você escolheu ARCO E FLECHA. Esperamos que tenha uma boa mira... ")
            for ch in arco:
                time.sleep(0.1) 
                print(ch, end='', flush=True)
        elif escolha_arma == "3":
            contador.incrementar(25)
            print()
            espada = ("Você escolheu ESPADA. Esperamos que você seja habilidoso... ")
            for ch in espada:
                time.sleep(0.1) 
                print(ch, end='', flush=True)
        elif escolha_arma == "4":
            contador.incrementar(20)
            print()
            sabre = ("Você escolheu SABRE DE LUZ. Esperamos QUE A FORÇA ESTEJA COM VOCÊ... ")
            for ch in sabre:
                time.sleep(0.1) 
                print(ch, end='', flush=True)
        elif escolha_arma == "5":
            contador.incrementar(30)
            print()
            foice = ("Você escolheu FOICE. TODO MUNDO EM PÂNICO AGORA... ")
            for ch in foice:
                time.sleep(0.1) 
                print(ch, end='', flush=True)
        elif escolha_arma == "6":
            contador.incrementar(50)
            print()
            tridente = ("Você escolheu TRIDENTE DE POSEIDON. Esperamos que saiba nadar... Continue a nadar... Continue a nadar...\n")                    
            for ch in tridente:
                time.sleep(0.1) 
                print(ch, end='', flush=True)
            Asciis.dory()
        print()
        