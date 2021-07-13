# Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

l = [5, 7, 2, 9, 4, 1, 3]
print (f"Lista para manipulação ==> {l}")
print()
print (f"O tamanho da lista é de {len(l)} itens")
print(f"O maior valor da lista é {max(l)}")
print (f"O menor valor da lista é {min(l)}")
print(f"A soma de todos os itens da lista é {(sum(l))}")
print(f"Lista em ordem crescente: {sorted(l)}")
l.sort(reverse=True)
print(f"Lista em ordem decrescente: {l}")
