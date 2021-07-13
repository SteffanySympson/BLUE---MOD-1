# Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
# escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

import random
from time import sleep

def inicial ():
    from time import sleep 
    print ("="*40)
    print ("              JOGO DA FORCA   ")
    print('-'*40)
    print ("          By STEFFANY SYMPSON")
    print('-'*40)
    print ("           The Future is Blue")
    print ("="*40)
    sleep(0.8)
    print("Vamos Jogar?")
    sleep(0.8)
    print("Boa Sorte...")
    sleep(0.8)
    print("Let")
    sleep(0.8)
    print("it")
    sleep(0.8)
    return "GO!"
def enforcado (erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    return"_|___         "
def vencedor():
    print()
    print(" Parabéns, você ganhou! ")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    return" "
def perdeu():
    print("Você foi enforcado!")
    print("    _______________       ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    return"       \_______/           "
def forca ():
    palavras = open("./Desafios/forca.txt","r") 
    palavras = palavras.readlines()  
    erros = 0
    forca = random.choice(palavras).strip().upper() 
    print("A palavra escolhida é: ", end=("")) 
    for letra in forca: 
        print(f"_", " ",end = "") 
    print()
    conjunto_letras_forca=set(forca) 
    conjunto_letras_digitadas=set()

    while not (conjunto_letras_forca.issubset (conjunto_letras_digitadas)) and erros < 7: 
        print()
        letra_digitada = str(input("Digite seu palpite: ").upper())
        conjunto_letras_digitadas.add(letra_digitada)
        if letra_digitada in conjunto_letras_forca:
            print("A palavra escolhida é: ", end=(""))
            for letra in forca:
                if letra in conjunto_letras_digitadas:
                    print(letra, end="")
                else:
                    print(f"_ ", end ="")
        else:
            erros += 1
            print(enforcado(erros))
            print(f"==> Você errou {erros} de 6 tentativas!!! Fique atento!!! ")
        print()
        print('Letras já digitadas: ', conjunto_letras_digitadas)
    if erros > 6:
        sleep(1)
        print("pooooxa....")
        sleep (1)
        print(f"A palavra era {forca}")
        sleep(1)
        print(perdeu())
    elif (conjunto_letras_digitadas.issubset (conjunto_letras_forca)) and erros < 7:
        print (vencedor())   
    return" " 
       
print(inicial())
print(forca())        