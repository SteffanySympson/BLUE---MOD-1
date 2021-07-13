# Crie um programa que leia nome, sexo biologico e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

print("="*20)
print("    Cadastrando...        ")
print("="*20)
print()
dic_infos = {}
quant_pessoas = 0
idade_pessoas = 0
lista_mulheres = []
lista_idades_acima_media = []
while True:
    lista = []
    nome = str(input('Digite o seu nome: ').upper().strip())
    quant_pessoas += 1
    sexo = str(input('Informe o seu sexo: [F/M] ').upper().strip()[0])
    lista.append(sexo)
    while sexo not in 'MF':
        sexo = str(input('Informe o seu sexo: [F/M] ').upper().strip()[0])
    if sexo == 'F':
        lista_mulheres.append(nome)
    idade = int(input('Informe a sua idade: '))
    idade_pessoas += idade
    lista.append(idade)
    dic_infos[nome] = lista
    continuar = str(input('Deseja continuar? [S/N] ').upper().strip()[0])
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ').upper().strip()[0])
    if continuar == 'N':
        break
media_idades = int((idade_pessoas / quant_pessoas))
for i in dic_infos:
    if dic_infos[i][1] > media_idades:
        lista_idades_acima_media.append(dic_infos[i][1])

print()
print(dic_infos)
print()
print(f'Total de cadastros: {quant_pessoas}')
print(f'Média de idades: {media_idades} anos')
print(f'Mulheres Cadastradas: {lista_mulheres}')
print(f'Idades acima da média: {lista_idades_acima_media}')