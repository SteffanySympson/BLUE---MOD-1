# 04 - Desenvolva um código em que o usuário vai entrar vários números e no final vai apresentar a
# soma deles (o usuário vai dizer quantos números serão informados antes de começar)

print ("Programa de somas")
print ()

soma = 0
quantidade = int (input ("Quantos números vamos somar?"))

for i in range(quantidade):
    soma = soma + int (input ("Digite a entrada numérica: "))
print( "O  valor da soma é:", soma)