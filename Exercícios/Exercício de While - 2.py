# Escreva um programa que pede a senha uma senha ao usuário, e só sai do loop quando digitarem
# corretamente a senha. A senha é “Blue123”
# Exiba quantas vezes o usuário errou a digitação.

print ("Open Program. Welcome!")
print()
senha = "Blue123"
entrada = ""
erro = 1

while entrada != senha:
    entrada = input("Digite a senha:\n")
    print("Tentativa: ", erro)
    erro += 1

    if entrada == senha:
        print ("Acesso liberado!")
        break

    if erro == 4:
        print("Você tem apenas mais um chance.")
    elif erro > 4:
        print ("Número de tentativas excedidas.")
        break
