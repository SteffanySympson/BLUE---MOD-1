# Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, 
# se seu argumento for negativo e ‘0’ se for 0.

def argumento(valor):
    if valor > 0:
        return 'P'
    elif valor < 0:
        return 'N'
    elif valor == 0:
        return 0
    else:
        return 'Argumento inválido'

numero = int(input('Digite um número: '))

print(argumento(numero))
