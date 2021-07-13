# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No
# final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

# contador para maior de 18 anos
# contador para homens
# contador para mulheres com menos de 20
# um input com sedo e idade
# um while infinito enquanto a resposta para a entrada for S 

genero_M = 0
genero_F_20 = 0
idade_18 = 0
cadastramento = 0

print ("PROGRAMA DE CADASTRAMENTO")
print ()
cadastro = input("Deseja iniciar um cadastramento (Resp. S / N):\n").upper()
print ()

while cadastro == "S":
  genero = input("Informe o gênero (F / M):\n").upper()
  while genero != "M" and genero != "F":
    genero = input("Entrada não permitida, insira uma entrada válida (M/F).")
    genero = genero.upper()
  idade = int (input("Informe a idade: "))
  cadastramento += 1
  cadastro = input("Deseja iniciar outro cadastramento (Resp. S / N):\n").upper()
  if genero == "M":
     genero_M += 1
  if idade > 18:
    idade_18 += 1
  if genero == "F" and idade < 20:
    genero_F_20 += 1
        
print(f"Existem {genero_M} homens cadastrados.\n")
print(f"Existem {idade_18} maiores de 18 anos cadastrado.\n")
print(f"Existem {genero_F_20} mulheres menores de 20 anos cadastradas. \n")
print(f"Existem {cadastramento} pessoas cadastradas.")