#3. Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
# A média para aprovação é 7.
# Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.

print ("="*50)
print ("Analisando aprovação através de Dicionário")
print ("="*50)
print()
dic_media = {}

while True:
    nome = str(input('Digite o nome do aluno: [Digite 0 para encerrar] ').title().strip())
    if nome == '0':
        break
    media = float(input(f'Digite a média do(a) {nome}: ').replace(',','.').strip())
    dic_media[nome] = media
    if dic_media[nome] >= 7:
        print('Aprovado')
    elif dic_media[nome] >= 5 and dic_media[nome] <= 6.9:
        print('Recuperação')
    elif dic_media[nome] < 5:
        print('Reprovado')

print(dic_media)

