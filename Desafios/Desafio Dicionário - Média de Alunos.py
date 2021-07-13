# Crie agora um boletim escolar, seu programa deve receber 5 notas de 15 alunos,
# assim como o nome desses alunos, o programa tem que calcular a # média desse aluno e
# mostrar a situação dele, seguindo os mesmos critérios apresentados no exercício 3. 
# No final apresente todos nomes, as 5 notas, as médias e as situações dos 15 alunos de uma vez só.

dic_alunos = {}

while True:
    lista = []
    nome = str(input('Digite o nome do aluno: ').title())
    soma_notas = 0
    for n in range(5):
        nota = float(input(f'Digite a nota da {n+1}ª avaliação: ').replace(',','.'))
        lista.append(nota)
        soma_notas += nota
    media = soma_notas / 5
    if media >= 7:
        lista.append('Aprovado')
    elif media >= 5 and media <= 6.9:
        lista.append('Recuperação')
    elif media < 5:
        lista.append('Reprovado')
    lista.append(media)
    dic_alunos[nome] = lista
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
print()
for i in dic_alunos:
    print(f'Aluno(a): {i}\n1ª avaliação = {dic_alunos[i][0]}\n2ª avaliação = {dic_alunos[i][1]}\n3ª avaliação = {dic_alunos[i][2]}\n4ª avaliação = {dic_alunos[i][3]}\n5ª avaliação = {dic_alunos[i][4]}\nMédia = {dic_alunos[i][6]}\nSituação {dic_alunos[1][5]}')
