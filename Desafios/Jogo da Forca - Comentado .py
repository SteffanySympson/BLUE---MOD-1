# Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
# escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
#variável erro para contar os erros do usuário
#importar uma lista de um bloco de notas
#escolher aleatoriamente

#Abra as DEFs para ler os comentários explicativos

import random
from time import sleep

def inicial ():
    from time import sleep #para usar o sleep dentro da função eu tenho q importar ele dentro dela.
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
    palavras = open("./Desafios/forca.txt","r") #abrindo o arquivo externo com as palavras para o sorteio. # veja a respeito de esquema de relative path.
    palavras = palavras.readlines() #readline faz com que o arquivo seja lido e colocado linha a linha 
    erros = 0
    forca = random.choice(palavras).strip().upper() #escolher palavras aleatoriamente
    print("A palavra escolhida é: ", end=("")) # comando end serve para que ele não pule a linha. Deixar aspas sem espaço.
    for letra in forca: #forca é a variável que contém a palavra sorteada aleatoriamente da lista externa.
        print(f"_", " ",end = "") #o for percorre a palavra e troca cada letra por um traço e um espaço
    print()
    conjunto_letras_forca=set(forca) # Um conjunto (set) é um tipo de dados de coleção, suportando o operador de associação in, a função len() e é iterável. 
    # Conjuntos não possuem noção de ordem por isso seus elementos não podem ser acessados com colchetes [] nem podem ser fatiados.
    # Os conjuntos (set) não aceitam valores repetidos ao tentar criar um conjunto com valores repetidos eles serão descartados só sobrando um valor do mesmo.
    #Podemos ainda criar conjuntos a partir de uma lista ou tupla com set
    # O conjunto permite a realização de operações matemáticas comparativas, como por exemplo argumentar se um conjunto está contindo em outro, se uma variável está contida em um conjunto, etc. Como na época da escola.
    # Conjunto permite ações comparativas.
    conjunto_letras_digitadas=set()

    while not (conjunto_letras_forca.issubset (conjunto_letras_digitadas)) and erros < 7: #issubset (é sub conjunto de.... está em...) é uma ação comparativa
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
    elif (conjunto_letras_digitadas.issubset (conjunto_letras_forca)) and erros < 7: #Não pode igualar os conjuntos, ele sempre dará errado uma vez que o conjunto de letras digitadas vai conter os erros e tbm os acertos do jogador. É preciso comparar se o conjunto de letras digitadas é um SUBCONJUNTO, ou seja, se ele está contido no conjunto de letras da forca.
        print (vencedor())   
    return" " 
       
print(inicial())
print(forca())        