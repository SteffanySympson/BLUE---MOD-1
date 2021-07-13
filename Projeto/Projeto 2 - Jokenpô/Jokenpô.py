# crie um programa que jogue pedra, papel e tesoura (Jokenpô) com você. O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha de quantidade de rodadas, se não finalize o programa.

from random import randint
from time import sleep

print("=-"*8, "\U0000270C","\U0000270B","\U0000270A","=-"*8)
print("JOKENPÔ   ----   BY:  STEFFANY SYMPSON")
print("=-"*8, "\U0000270C","\U0000270B","\U0000270A","=-"*8)
print()
print("Seja Bem Vindo!\n")

continuacao = 0
contadorpc = 0
contadorjogador = 0
contadorempate = 0

while continuacao != "NAO":
    rodadas = int(input("Quantas rodadas vamos jogar?\n"))
    print("="*30)
    print(f"Faremos uma melhor de {rodadas}!")
    print("="*30)
    sleep(0.5)
    print()
    for i in range (rodadas):
        opcoes = ("Pedra", "Papel", "Tesoura")
        pc = randint (0,2)
        perguntar = int(input('''Faça sua escolha: 

        [0] Pedra 
        [1] Papel
        [2] Tesoura
            
        Digite sua escolha: '''))
        print("\U0001F64A")
        print("JO...")
        sleep(1)
        print("\U0001F649")
        print("...KEN...")
        sleep(1)
        print("\U0001F648")
        print("...POOH!!!")
        sleep(0.4)
        print("=*"*14)
        print("O COMPUTADOR escolheu {}".format(opcoes[pc]))
        print()
        print("VOCÊ escolheu {}".format(opcoes[perguntar]))
        print("=*"*14)
        print()
        if pc == 0:
            if perguntar == 0:
                print("EMPATE!\n")
                contadorempate +=1
            elif perguntar == 1:
                print ("Você Venceu! *-*\n")
                contadorjogador +=1
            elif perguntar == 2:
                print ("Você perdeu! \n") 
                contadorpc +=1
            else: 
                print("Inválido!")
        elif pc == 1:
            if perguntar == 0:
                print ("Você perdeu! \n")
                contadorpc +=1
            elif perguntar == 1:
                print ("EMPATE!\n")
                contadorempate +=1
            elif perguntar == 2:
                print ("Você Venceu! *-*\n")
                contadorjogador +=1
            else:
                print ("Inválido") 
        elif pc == 2:
            if perguntar == 0:
                print ("Você Venceu! *-*\n")   
                contadorjogador +=1
            elif perguntar == 1:
                print ("Você perdeu! \n")
                contadorpc +=1
            elif perguntar == 2:
                print("EMPATE!\n")
                contadorempate +=1
            else:
                print ("Inválido!")      
        else:
            print("Opção inválida!")
    if contadorjogador > contadorpc:
        print()
        print("=-"*10)
        print("VOCÊ VENCEU!!!  " "\U0001F60D")
        print(f"Você venceu {contadorjogador} vezes.")
        print(f"O Computador venceu {contadorpc} vezes.")
        print(f"Vocês empataram {contadorempate} vezes.")
    elif contadorpc > contadorjogador:
        print()
        print("=-"*10)
        print("VOCÊ PERDEU!!!  ", "\U0001F622")
        print(f"Você venceu {contadorjogador} vezes.")
        print(f"O Computador venceu {contadorpc} vezes.")
        print(f"Vocês empataram {contadorempate} vezes.")
    elif contadorempate > contadorjogador and contadorempate > contadorpc:
        print()
        print("=-"*10)
        print("DEU EMPATE!!!", "\U0001F646")
        print(f"Você venceu {contadorjogador} vezes.")
        print(f"O Computador venceu {contadorpc} vezes.")
        print(f"Vocês empataram {contadorempate} vezes.")
    continuacao = str(input("Deseja jogar novamente ?\n").upper().replace("Ã","A"))  