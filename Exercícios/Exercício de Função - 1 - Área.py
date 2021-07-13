# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno:

def area (b, h):
    multiplicar = b*h
    print(f'O Valor da área é {multiplicar} m².')

print(" Calculo de área")
print()
b = (float(input("Informe o valor da base: ")))
h = (float(input("Informe o valor da altura: ")))
area(b,h)
