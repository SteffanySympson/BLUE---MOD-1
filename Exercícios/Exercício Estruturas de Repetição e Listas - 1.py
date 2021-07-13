# Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

#imput de int
# se x == x não dar imput
#print da lista

lista = []
entrada = 0

pergunta = str(input('Deseja inserir um número ? S/N ').upper())
while pergunta[0] == 'S':
    entrada = int(input('Digite o valor: '))
    pergunta = str(input('Deseja continuar ? S/N ').upper())
    if entrada in lista:
        pass
    else: 
        lista.append(entrada)

lista.sort()
print(lista)


