#1.	Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma
# desses três argumentos.

def somar(n1,n2,n3):
    soma = n1 + n2 + n3
    return soma

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

print(f'A soma dos 3 números é: {somar(num1,num2,num3)}')
