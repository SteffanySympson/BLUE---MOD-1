# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
# artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print("=="*20)
print("  * * * * FOGOS DE ARTIFCÍCIO * * * *")
print("=="*20)
print()

for i in range(10,0, -1):
    print(i)
    sleep(1)
print("*!"*30)
    