# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioraidade e quantas já são
# maiores.
 

print("=="*20)
print("   * * * * Será Maior de 18? * * * *")
print("=="*20)
print()

ano = []
menores = []
contador = 0
contador2 = 0

for i in range(0,7):
    n = int(input("Digite o ano de nascimento: "))
    ano.append(n)
    ano.sort()
    maioridade = (2021 - n) 
    print(f"Idade: {2021 - n}")
    if maioridade < 18:
        menores.append(n)
        menores.sort()
        contador += 1
    else:
        contador2 += 1
print()
print("O anos informados são: ", ano)
print()
print(f"São menores de idade: {contador} pessoas.")
print(f"Nascidas em: {menores}")
print()
print(f"São maiores de idade: {contador2} pessoas.")
