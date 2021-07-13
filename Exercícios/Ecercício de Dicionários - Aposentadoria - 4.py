# 4. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se
# aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.


dic_ctps = {}
ano = 2021

while True:
    lista = []
    nome = str(input("Digite o nome do trabalhador [Digite 0 para finalizar]: "))
    if nome == "0":
        break
    ano_nascimento = int(input(f"Ano de nascimento do(a) {nome}: "))
    lista.append(ano_nascimento)
    idade = ano - ano_nascimento
    lista.append(f"{idade} anos")
    ctps = int(input("Digite o número da CTPS: "))
    lista.append(f"número da CTPS: {ctps}")
    if ctps != 0:
        ano_contratacao = int(input("Ano de contratação: "))
        lista.append(f"Ano de contratação: {ano_contratacao}")
        salario = (float(input("Salário: R$")).replace()
        lista.append(f"Salário: R$ {salario}")
        tempo_contribuicao = ano - ano_contratacao
        lista.append(f"{tempo_contribuicao} anos de contribuição")
        if tempo_contribuicao >= 35:
            print("Apto para aposentadoria.")
        else:
            tempo_restante_apos = 35 - tempo_contribuicao
            print(f"Falta (m) {(tempo_restante_apos)} ano (s).")
            print(f"Aposentadoria com {tempo_restante_apos + idade} anos.")
    dic_ctps[nome] = lista
print(dic_ctps)
