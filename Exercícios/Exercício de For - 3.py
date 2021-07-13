# Faça um script que o usuário escolha um número de início, um número de fim, e um número de
# passo. O programa deve printar todos os números do intervalo entre início e fim, "pulando" de
# acordo com o intervalo passado.

print("="*20)
print("Exercício do Passo")
print("="*20)
print()

m = int(input("Informe o número de início: "))
n = int(input("Informe o número final: "))
p = int(input("Informe o passo da contagem: "))

for i in range (m, n, p):
    print (i)