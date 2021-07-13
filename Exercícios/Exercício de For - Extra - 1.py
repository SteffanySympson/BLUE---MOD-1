# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.

print("=="*20)
print("   * * * * LEITORA DE PESO * * * *")
print("=="*20)
print()

peso = []

for i in range(0,5):
    n = (input("Digite o peso: ")).replace(",",".")
    peso.append(n)
print("Os pesos informados são: ", peso)
print("O menor peso imputado é: ", min(peso), "KG.")
print("O maior peso imputado é: ", max(peso), "KG.")