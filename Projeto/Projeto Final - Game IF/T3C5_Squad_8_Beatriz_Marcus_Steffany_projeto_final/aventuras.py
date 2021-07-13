from asciis import Asciis
from music import musica

class Aventuras:

    def cont_golpe (ano):
        from datetime import date
        atual = date.today().year
        golpe = atual - ano
        return golpe
        
    def AventPraia(self, monstro, contador):
        import time
        from random import randint
        print()
        monstro = ('Sua aventura na praia está para ficar animada. Ao longe podemos ver o Godzilla e uma Lula Gigante.')
        for ch in monstro:
            time.sleep(0.1) 
            print(ch, end='', flush=True)
        print()
        Asciis.godz()
        escolha_monstro = input('\n[1] Enfrentar o Godzilla\n[2] Enfrentar a Lula\nQual monstro vamos enfrentar? ')
        while escolha_monstro not in ['1','2']:
            print('Opção inválida!')
            escolha_monstro = input('\n[1] Enfrentar o Godzilla\n[2] Enfrentar a Lula\nQual monstro vamos enfrentar? ')        
        if escolha_monstro == "1":
            string1 = ('\nVocê não pode ganhar do Godzilla, pois você não é o Kong! Mas pode deixar ele tonto e aproveitar para fugir.')
            for ch in string1:
                time.sleep(0.1) 
                print(ch, end='', flush=True)
            num = randint(0,30)
            print()
            string2 = ('\nVocê tropeçou em um tronco. Ele te mostrou quantos golpes você vai precisar acertar em Godzilla para conseguir fugir. Use a sua arma para atingir e atordoar o Godzilla.')
            for ch in string2:
                time.sleep(0.1) 
                print(ch, end='', flush=True)
            print()
            print(f'\n====> Golpes Necessários ====> {num}')
            print()
            ano = int(input ('Curiosidade... Em que ano você nasceu? '))
            contador_de_golpes = Aventuras.cont_golpe(ano)
            if contador_de_golpes == num:
                string3 = ('\nOpaaaa! Acertou em cheio!\n\nVocê está diante de dois caminhos:')
                for ch in string3:
                    time.sleep(0.1) 
                    print(ch, end='', flush=True)                              
                caminho = input('\n[1] Caminho das conchas amarelas\n[2] Caminhos das estrelas\nQual você escolherá? ')
                while caminho not in ['1','2']:
                    print('Opção inválida!')
                    caminho = input('\n[1] Caminho das conchas amarelas\n[2] Caminhos das estrelas\nQual você escolherá? ')
                if caminho == '1':
                    contador.incrementar(1000)
                    string4 = (f'\nSua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois dias...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
                    for ch in string4:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
                elif caminho == '2':
                    contador.incrementar(2000)
                    string4 = (f'\nSua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois minutos...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
                    for ch in string4:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
            elif contador_de_golpes > num:
                string5 = ('\nNOCAUTE!\n\nVocê está diante de dois caminhos: ')
                for ch in string5:
                    time.sleep(0.1) 
                    print(ch, end='', flush=True)                              
                caminho = input('\n[1] Caminho das conchas amarelas\n[2] Caminhos das estrelas\nQual você escolherá? ')
                while caminho not in ['1','2']:
                    print('Opção inválida!')
                    caminho = input('\n[1] Caminho das conchas amarelas\n[2] Caminhos das estrelas\nQual você escolherá? ')
                if caminho == '1':
                    contador.incrementar(1000)
                    string4 = (f'\nSua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois dias...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
                    for ch in string4:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
                elif caminho == '2':
                    contador.incrementar(2000)
                    string4 = (f'\nSua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois minutos...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
                    for ch in string4:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
            elif contador_de_golpes < num:
                string6 = ("\nUooowwwww... foi perto... corra....corra!!!!\n\nVocê está diante de dois caminhos: ")
                for ch in string6:
                    time.sleep(0.1) 
                    print(ch, end='', flush=True)                             
                caminho = input('\n[1] Caminho das conchas amarelas\n[2] Caminhos das estrelas\nQual você escolherá? ')
                while caminho not in ['1','2']:
                    print('Opção inválida!')
                    caminho = input('\n[1] Caminho das conchas amarelas\n[2] Caminhos das estrelas\nQual você escolherá? ')
                if caminho == '1':
                    contador.incrementar(1000)
                    string4 = (f'\nSua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois dias...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
                    for ch in string4:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
                elif caminho == '2':
                    contador.incrementar(2000)
                    string4 = (f'\nSua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois minutos...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
                    for ch in string4:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)   
        elif escolha_monstro == "2":
            string7 = ("\nLula nada... Lula solta tinta... Tem 8 braços e 2 tentáculos... Afogue ela na areia ou não volte para casa! Use sua super arma esolhida no início do jogo")
            for ch in string7:
                time.sleep(0.1) 
                print(ch, end='', flush=True)  
            num = randint(0,30)
            string8 = ("\nVocê bateu em um coral... Ele te mostrou quantos golpes vai precisar acertar na Lula com sua super arma para conseguir fugir...Use-a sabiamente para ganhar a batalha!!!")
            for ch in string8:
                time.sleep(0.1) 
                print(ch, end='', flush=True)            
            print(f'\n\n====> Golpes Necessários ====> {num}')
            print()
            ano = int(input ('Curiosidade... Em que ano você nasceu? '))
            contador_de_golpes = Aventuras.cont_golpe(ano)
            if contador_de_golpes == num:
                string9 = ('\nOpaaa!!! Acertou em cheio!!! Tinta e espetinho de Lula para todos os lugares!\nVocê está diante de dois caminhos: ')
                for ch in string9:
                    time.sleep(0.1) 
                    print(ch, end='', flush=True)
                print()              
                caminho = input('\n[1] Caminho das conchas amarelas\n[2] Caminhos das estrelas\nQual você escolherá? ')
                while caminho not in ['1','2']:
                    print('Opção inválida!')
                    caminho = input('\n[1] Caminho das conchas amarelas\n[2] Caminhos das estrelas\nQual você escolherá? ')
                if caminho == '1':
                    contador.incrementar(1000)
                    string4 = (f'\nSua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois dias...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
                    for ch in string4:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
                elif caminho == '2':
                    contador.incrementar(2000)
                    string4 = (f'\nSua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois minutos...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
                    for ch in string4:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
                elif caminho == '2':
                    contador.incrementar(2000)
                    string4 = (f'Sua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois minutos...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
            elif contador_de_golpes > num:
                string5 = ('NOCAUTE!\nVocê está diante de dois caminhos: ')
                for ch in string5:
                    time.sleep(0.1) 
                    print(ch, end='', flush=True)
                print()              
                caminho = input('\n[1] Caminho das conchas amarelas\n[2] Caminhos das estrelas\nQual você escolherá? ')
                while caminho not in ['1','2']:
                    print('Opção inválida!')
                    caminho = input('\n[1] Caminho das conchas amarelas\n[2] Caminhos das estrelas\nQual você escolherá? ')
                if caminho == '1':
                    contador.incrementar(1000)
                    string4 = (f'\nSua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois dias...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
                    for ch in string4:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
                elif caminho == '2':
                    contador.incrementar(2000)
                    string4 = (f'\nSua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois minutos...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
                    for ch in string4:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
            elif contador_de_golpes < num:
                string10 = ("Uooowwwww... foi perto... nada....nada!\n Você está diante de dois caminhos: ")
                for ch in string10:
                    time.sleep(0.1) 
                    print(ch, end='', flush=True)
                print()              
                caminho = input('\n[1] Caminho das conchas amarelas\n[2] Caminhos das estrelas\nQual você escolherá? ')
                while caminho not in ['1','2']:
                    print('Opção inválida!')
                    caminho = input('\n[1] Caminho das conchas amarelas\n[2] Caminhos das estrelas\nQual você escolherá? ')
                if caminho == '1':
                    contador.incrementar(1000)
                    string4 = (f'\nSua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois dias...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
                    for ch in string4:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
                elif caminho == '2':
                    contador.incrementar(2000)
                    string4 = (f'\nSua riqueza chegou a {contador.valor} moedas. Você chegará em casa em dois minutos...\nFoi muito bom jogar com você! Nos vemos na nossa próxima aventura!')
                    for ch in string4:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)             

    def AventMontanha(self, viagem_tempo, contador):
        import time
        from random import randint
        string1 = ('\nNão há nada melhor que encontrar uma caverna escura, vazia e úmida no meio de um passeio pelas montanhas.\n◔_◔\nEra um segredo, mas no fundo dessa caverna há um buraco de minhoca que te levará:')
        for ch in string1:
            time.sleep(0.1) 
            print(ch, end='', flush=True)
        Asciis.choice()
        viagem_tempo = input("\n[1] 33 anos no passado\n[2] 33 anos no futuro\nFaça sua escolha: ")
        while viagem_tempo not in ['1','2']:
            print('Opção inválida!')
            viagem_tempo = input("\n[1] 33 anos no passado\n[2] 33 anos no futuro\nFaça sua escolha: ")
        if viagem_tempo == "1":            
            string2 = ('\nVocê está no momento do primeiro e único lançamento do ônibus espacial soviético. VAMOS AO ESPAÇO!!!')
            for ch in string2:
                time.sleep(0.1) 
                print(ch, end='', flush=True)
            escolhaET = input('\n[1] Dê um alô aos ETs\n[2] Darth Vader\nCom quem você terá seu super encontro espacial? ')
            while escolhaET not in ['1','2']:
                print('Opção inválida!')
                escolhaET = input("\n[1] Dê um alô aos ET's\n[2] Darth Vader\nCom quem você terá seu super encontro espacial? ")
            if escolhaET == '1':
                string3 = ('\nNo espaço, ninguém pode ouvir você gritar... Já dizia o oitavo passageiro...')
                for ch in string3:
                    time.sleep(0.1) 
                    print(ch, end='', flush=True)
                contador.incrementar(-1000)
                print()
                string4 = ("\nO ET era o Alien, pena que você não é o Predador. Nos vemos na próxima...\nGAME OVER!")
                for ch in string4:
                    time.sleep(0.1) 
                    print(ch, end='', flush=True)
                print()
                musica(True)
                Asciis.gameover()  
            elif escolhaET == '2':
                string5 = ("\nLuke, I'm your father!\nVocê está indignado então vamos a batalha!")
                for ch in string5:
                    time.sleep(0.1) 
                    print(ch, end='', flush=True)
                Asciis.darth()
                num = randint(0,30)                
                print(f'\n====> Golpes Necessários ====> {num}')
                print()
                ano = int(input('Curiosidade... Em que ano você nasceu? '))
                contador_de_golpes = Aventuras.cont_golpe(ano)
                if contador_de_golpes == num:
                    string6 = ('\nOpaaa! Acertou em cheio! Você ganhou do Darth Vader!\nVocê está diante de dois caminhos:')
                    for ch in string6:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
                    caminho = input('\n[1] Millennium Falcon\n[2] Executor\nQual você escolherá? ')
                    while caminho not in ['1','2']:
                        print('Opção inválida!')
                        caminho = input('\n[1] Millennium Falcon\n[2] Executor\nQual você escolherá? ')
                    if caminho == '1':
                        contador.incrementar(2000)
                        string7 = (f'\nVocê escolheu a melhor nave da galáxia...Seu retorno será ESTELAR...Sua riqueza chegou a {contador.valor} moedas, você estará de volta em casa em 1 dia!!!\nFoi muito bom jogar com você!!! Nos vemos na nossa próxima aventura!!!')
                        for ch in string7:
                            time.sleep(0.1) 
                            print(ch, end='', flush=True)
                    elif caminho == '2':
                        contador.incrementar(1000)
                        string8 = (f'\nEssa nave já viu dias melhores...Sua riqueza chegou a {contador.valor} moedas, você chegará em casa em 2 anos...\nFoi muito bom jogar com você!!!Nos vemos na nossa próxima aventura!!!')
                        for ch in string8:
                            time.sleep(0.1) 
                            print(ch, end='', flush=True)
                elif contador_de_golpes > num:
                    string9 = ('\nNOCAUTE!!!\nVocê ganhou do Darth... Você está diante de dois caminhos:')
                    for ch in string9:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
                    caminho = input('\n[1] Millennium Falcon\n[2] Executor\nQual você escolherá? ')
                    while caminho not in ['1','2']:
                        print('Opção inválida!')
                        caminho = input('\n[1] Millennium Falcon\n[2] Executor\nQual você escolherá? ')
                    if caminho == '1':
                        contador.incrementar(2000)
                        string7 = (f'\nVocê escolheu a melhor nave da galáxia...Seu retorno será ESTELAR...Sua riqueza chegou a {contador.valor} moedas, você estará de volta em casa em 1 dia!!!\nFoi muito bom jogar com você!!! Nos vemos na nossa próxima aventura!!!')
                        for ch in string7:
                            time.sleep(0.1) 
                            print(ch, end='', flush=True)
                    elif caminho == '2':
                        contador.incrementar(1000)
                        string8 = (f'\nEssa nave já viu dias melhores...Sua riqueza chegou a {contador.valor} moedas, você chegará em casa em 2 anos...\nFoi muito bom jogar com você!!!Nos vemos na nossa próxima aventura!!!')
                        for ch in string8:
                            time.sleep(0.1) 
                            print(ch, end='', flush=True)
                elif contador_de_golpes < num:
                    string10 = ("\nUooowwwww... foi perto... Corra, Luke! Corra!\nVocê não ganhou do Darth... Mas conseguiu fugir... Você está diante de dois caminhos: ")
                    for ch in string10:
                        time.sleep(0.1) 
                        print(ch, end='', flush=True)
                    caminho = input('\n[1] Millennium Falcon\n[2] Executor\nQual você escolherá? ')
                    while caminho not in ['1','2']:
                        print('Opção inválida!')
                        caminho = input('\n[1] Millennium Falcon\n[2] Executor\nQual você escolherá? ')
                    if caminho == '1':
                        contador.incrementar(2000)
                        string7 = (f'\nVocê escolheu a melhor nave da galáxia...Seu retorno será ESTELAR...Sua riqueza chegou a {contador.valor} moedas, você estará de volta em casa em 1 dia!!!\nFoi muito bom jogar com você!!! Nos vemos na nossa próxima aventura!!!')
                        for ch in string7:
                            time.sleep(0.1) 
                            print(ch, end='', flush=True)
                    elif caminho == '2':
                        contador.incrementar(1000)
                        string8 = (f'\nEssa nave já viu dias melhores...Sua riqueza chegou a {contador.valor} moedas, você chegará em casa em 2 anos...\nFoi muito bom jogar com você!!!Nos vemos na nossa próxima aventura!!!')
                        for ch in string8:
                            time.sleep(0.1) 
                            print(ch, end='', flush=True)
        elif viagem_tempo == "2":
            string3 = ("\nVocê foi assassinado e agora é um fantasma sem memória...\nVocê precisa descobrir a arma do crime, se conseguir pode voltar a vida...Se não....")
            for ch in string3:
                time.sleep(0.1)
                print(ch, end='', flush=True)
            print()
            print("Esses são os cenários: ")
            time.sleep(0.1)
            print('[1] Sala ==> Piano com um copo vazio... Um buquê de flores sem remetente... Você pode ter bebido o que não devia ou colocado o nariz onde não foi chamado... SERÁ QUE VOCÊ MORREU ENVENENADO?')
            time.sleep(0.1)
            print('[2] Quarto ==> Uma almofada no chão e a cama desfeita... Vc dormia... Um bilhete no chão... Tem sangue no chão e uma faca no banheiro... SERÁ QUE VOCÊ MORREU ESFAQUEADO?')
            time.sleep(0.1)
            print('[3] Jardim ==> Duas taças de coquetel na piscina e uma gota de sangue... Um bilhete da polícia: Detetive John Doe esteve aqui... Uma arma sobre a toalha... SERÁ QUE VOCÊ MORREU BALEADO?')
            time.sleep(0.1)
            arma_crime = randint(1,3)
            aposta_arma_crime = int(input("\nO que diz o seu instinto? "))
            while aposta_arma_crime not in [1,2,3]:
                print('Opção inválida!')
                aposta_arma_crime = int(input("\nO que diz o seu instinto? "))
            if aposta_arma_crime == arma_crime:
                contador.incrementar(3000)
                string4 = (f"\nVocê é muito esperto!!!Descobriu a arma do crime, sua riqueza agora é {contador.valor}, e você conquistou a chance de voltar a vida... pague pelo túnel e Vá para luz!!! Foi bom jogar com você!!!")
                for ch in string4:
                    time.sleep(0.1)
                    print(ch, end='', flush=True)
            elif aposta_arma_crime != arma_crime:
                string5 = ('\nSeu instinto falhou. Você tem mais uma chance. Tente novamente!')
                for ch in string5:
                    time.sleep(0.1)
                    print(ch, end='', flush=True)
                aposta_arma_crime = int(input("\nO que diz o seu instinto? "))
                if aposta_arma_crime == arma_crime:
                    contador.incrementar(3000)
                    string6 = (f"\nVocê é muito esperto!!!Descobriu a arma do crime, sua riqueza agora é {contador.valor} moedas e você conquistou a chance de voltar a vida... entre no túnel e Vá para luz!!! Foi bom jogar com você!!!")
                    for ch in string6:
                        time.sleep(0.1)
                        print(ch, end='', flush=True)
                elif aposta_arma_crime != arma_crime:
                    contador.incrementar(-3000)
                    string7 = (f"\nLamento... sua riqueza agora é {contador.valor} moedas. Você será um fantasma para sempre... Game Over... ")
                    for ch in string7:
                        time.sleep(0.1)
                        print(ch, end='', flush=True)