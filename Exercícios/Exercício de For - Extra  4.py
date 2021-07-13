# #Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Mostre também quantos valores pares foram digitados.

#input de inteiro q vai rodar 6 vezes
#se o input %2 == 0 soma
#printa lista com os inputs

numeros = []
soma = []
for i in range (0,6):
    n = int(input("Digite o número: "))
    numeros.append(n)
    if n %2 == 0:
        soma.append(n)
        total = sum(soma)
print(f"Os números digitados foram: {numeros}")
print(f"A Soma é {total}")