# Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.


lista = []
par = []
impar = []


pergunta = str(input('Deseja adicionar um número ? S/N ').upper())
while pergunta[0] == 'S':
    entrada = int(input('Digite o valor: '))
    pergunta = str(input('Deseja continuar ? S/N ').upper())
    if entrada in lista:
        pass
    else: 
        lista.append(entrada)
    if entrada % 2 == 0:
        par.append(entrada)
    else:
        impar.append(entrada)
lista.sort()
par.sort()
impar.sort()
print(lista)
print(par)
print(impar)
