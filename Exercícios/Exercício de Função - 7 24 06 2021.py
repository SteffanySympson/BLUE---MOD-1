# 7. Escreva uma função que recebe dois parâmetros e imprime o menor dos dois.
# Se eles forem iguais, imprima que eles são iguais.

def menor(num1,num2):
    if num1 < num2:
        return f'O {num1} é o menor'
    elif num2 < num1:
        return f'O {num2} é o menor'
    elif num1 == num2:
        return 'Os números são iguais'

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
print()
print(menor(num1,num2))
