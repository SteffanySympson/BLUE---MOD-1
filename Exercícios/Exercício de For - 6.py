# Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

print("=="*20)
print("       * * * * SEM VOGAIS * * * *")
print("=="*20)
print()

frase = input("Digite sua frase: ").upper()
    
for i in frase:
    if i == "A":
      frase = frase.replace("A", "")
    if i == "E":
      frase = frase.replace("E", "")
    if i == "I":
       frase = frase.replace("I", "")
    if i == "O":
      frase = frase.replace("O", "")
    if i == "U":
      frase = frase.replace("U", "")
print(frase)