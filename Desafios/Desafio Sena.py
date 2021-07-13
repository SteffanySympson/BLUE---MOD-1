# Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#um número deve ser randomizado
# lista principal
#contador
#enquanto for verdade repete

import random
from random import randint


print("        Roleta da Sorte Blue   -   JOGA NA MEGA!!!    ")
print()

quantidade = (int(input("Quantos jogos serão sorteados?")))
print()
TotalDeJogos = 1
jogos = []
lista = []


while TotalDeJogos <= quantidade:
    cont = 0 #o contador tem que estar dentro do 1º enquanto se não ele não roda 6 vezes nos loopins depois do 1º
    while True: #enquanto for verdade
        num = randint(1,60) #num será sorteado aleatoriamente entre 1 e 60 (mega sena não tem 0)
        if num not in lista: #se num não estiver contido na variável lista, faça:
            lista.append(num) #na variável lista, insira a variável num
            cont +=1 #cada vez que rodar insira mais um, soma mais um no contador
        if cont >= 6: #quando o contador chegar a 6
            break #pare de rodar
    lista.sort() #arruma decrescente a lista
    jogos.append(lista[:]) #[:] cria uma cópia da lista que foi sorteada
    lista.clear() #a variável lista é apagada a cada rodada do random, lembrando q ela está copiada dentro da lista jogos
    TotalDeJogos +=1 #para não entrar em looping eterno
print("        ", f".....SORTEANDO..... {quantidade}", ".....JOGOS.....")
for i, l in enumerate(jogos): #A função enumerate() retorna uma tupla (é igual a lista mas não pode ser modificada) de dois elementos a cada iteração: um número sequencial e um item da sequência correspondente.
   print(f"Jogo {i+1}: {l}")  
   print()
   print("BOA SORTE!!!")


