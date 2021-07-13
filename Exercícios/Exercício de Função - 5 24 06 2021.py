# 5. Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 
# e pese 75kg.

def imc(peso,altura):
    imc = peso / (altura*altura)
    return imc

peso = float(input('Informe o seu peso (em KG): ').replace(',','.'))
altura = float(input('Informe a sua altura (em Metros): ').replace(',','.'))

print(f'O seu IMC é: {imc(peso,altura):.2f}')
