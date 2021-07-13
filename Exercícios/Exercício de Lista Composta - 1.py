# 1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if,
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela
# a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade'
# e também quantos são maiores e quantos são menores de idade.

#input dos nomes
#input das idades
#criar a lista
#se maior q 18 printar maior de idade
#se menor q 18 printar menor de idade

print("=="*20)
print("   * * * * Será Maior de Idade? * * * *")
print("=="*20)
print()

lista_de_entradas = []
maior_idade = 0
menor_idade = 0

for a in range(5):
    while len (lista_de_entradas) < 5:
        lista_por_pessoa = []
        nome = (str(input("Digite o nome: "))).title()
        idade = int(input("Digite a idade: "))
        lista_por_pessoa.append(nome)
        lista_por_pessoa.append(idade)
        if idade <= 18:
            lista_por_pessoa.append("É menor de idade.")
            menor_idade += 1
        else:
            lista_por_pessoa.append("É maior de idade.")
            maior_idade += 1
        lista_de_entradas.append(lista_por_pessoa)
print()
for i in lista_de_entradas:
    print(f"Nome: {i[0]}, Idade: {i[1]}, {i[2]}")
print()
print(f"São menores de idade {menor_idade} pessoas.")
print(f"São maiores de idade {maior_idade} pessoas")



