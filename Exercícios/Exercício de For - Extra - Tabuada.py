# Crie um programa que pergunte ao usuário um número inteiro e faça a
# tabuada desse número.
from time import sleep
print("*_"*10)
print("       TABUADA")
print("*_"*10)
print()

tabuada = int(input("Informe o valor para a tabuada: "))

for num in range(11):
    print (f'{tabuada} x {num} = {tabuada*num}')
    sleep(1)