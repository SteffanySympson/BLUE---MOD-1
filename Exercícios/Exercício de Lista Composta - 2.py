# Faça um programa que leia nome e altura de várias pessoas, guardando tudo em uma lista,
# depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o
# programa. No final mostre:
# Quantas pessoas foram cadastradas
# Mostre a maior altura
# Mostre a menor altura

lista_de_entradas = []
cont_pessoas = 0
altura_maior = 0
altura_menor = 0
while True:
    entradas = []
    nome = str(input("Informe o nome: ")).title().strip()
    entradas.append(nome)
    cont_pessoas += 1
    altura = float(input("Informe a altura (em metros): ").replace(",","."))
    entradas.append(altura)
    if cont_pessoas == 1:
        altura_maior = altura
        altura_menor = altura
    else:
        if altura > altura_maior:
            altura_maior = altura
        if altura < altura_maior:
            altura_menor = altura
    lista_de_entradas.append(entradas)
    continuar = input("Deseja continuar cadastrando? S/N ").upper()
    while continuar not in "SN":
        continuar = input("Deseja continuar cadastrando? S/N ").upper()
    if continuar == "N":
        break
print()
print(lista_de_entradas)
print()
print(f"Total de pessoas cadastradas = {cont_pessoas}")
print(f"A maior altura cadastrada foi de {altura_maior} m.")
print(f"A menor altura cadastrada foi de {altura_menor} m.")
