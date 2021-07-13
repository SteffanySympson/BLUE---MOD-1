# Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


from random import randint
from time import sleep

print("        Roleta da Sorte Blue   -   JOGA NA MEGA!!!    ")
print()

quantidade = (int(input("Quantos jogos serão sorteados?")))
print()
TotalDeJogos = 1
jogos = []

while TotalDeJogos <= quantidade:
    cont = 0 
    lista= []
    while True: 
        num = randint(1,60) 
        if num not in lista: 
            lista.append(num) 
            cont +=1
        if cont >= 6: 
            break
    lista.sort()
    jogos.append(lista)
    TotalDeJogos +=1
print(f".....SORTEANDO..... {quantidade}", ".....JOGOS.....")
for i, l in enumerate(jogos): 
   print(f"Jogo {i+1}: {l}")  
   sleep(1)
print()
print("BOA SORTE!!!")