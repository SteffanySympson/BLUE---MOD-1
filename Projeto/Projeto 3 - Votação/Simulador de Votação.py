# Projeto 03 – Simulador de Votação
# Crie um programa que simule um sistema de votação, ele deve receber votos até que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá da função autoriza_voto()) e o voto que é o número que a pessoa votou. Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o contrário a 2° função deve validar o número que a pessoa escolheu, ela pode escolher de 1 a 5 (crie 3 candidatos para a votação):
# 1, 2 ou 3 - Votos para os respectivos candidatos
# 4- Voto Nulo
# 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# Qual candidato venceu a votação.
from time import sleep

def inicial ():
    print ("="*40)
    print ("              VOTAÇÃO   ")
    print('-'*40)
    print ("          By STEFFANY SYMPSON")
    print ("="*40)
    return("Vamos Votar?")   
def autoriza_voto (ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return "NEGADO"
    elif 16 <= idade < 18 or idade >65:
        return "OPCIONAL"
    else:
        return "OBRIGATÓRIO"
def opçao ():
    return f"Suas opções de votação são:\n Thor = 1\n Homem de Ferro = 2\n Hulk = 3\n Voto Nulo = 4\n Voto em Branco = 5"
def votacao (autorizacao, voto):
    autorizacao = autoriza_voto(nascimento)
    if autorizacao == "NEGADO":
        return f"Voto negado."
    elif autorizacao == "OBRIGATÓRIO" or autorizacao == "OPCIONAL":
        if voto == 1:
            candidatos["Thor"]  += 1
        elif voto == 2:
            candidatos["Homem de Ferro"] += 1
        elif voto == 3:
            candidatos["Hulk"] += 1
        elif voto == 4:
            candidatos["Nulo"] += 1
        elif voto == 5:
            candidatos["Branco"] += 1
    return f"Voto validado."

sleep(0.8)
print(inicial())
print()
sleep(0.8)

candidatos = {"Thor":0, "Homem de Ferro":0, "Hulk":0, "Nulo":0, "Branco":0}
while True:
    nascimento = int(input("Qual o ano do seu nascimento? [Digite 0 para encerrar]"))
    if nascimento == 0:
        break
    print()
    print(opçao())
    print()
    voto = int(input("Informe o número do seu candidato/voto: "))
    print()
    ano_autoriza = autoriza_voto(nascimento)
    print(votacao(ano_autoriza, voto))
    print()

print()
print(f'Resultado da votação:\n Thor {candidatos["Thor"]} votos\n Homem de Ferro {candidatos["Homem de Ferro"]} votos\n Hulk {candidatos["Hulk"]} votos\n Nulo {candidatos["Nulo"]} votos\n Branco {candidatos["Branco"]} votos')    
print()
if candidatos["Thor"] >  candidatos["Homem de Ferro"] and candidatos["Thor"] > candidatos["Hulk"] and candidatos["Thor"] > candidatos["Nulo"] and candidatos["Thor"] > candidatos["Branco"]:
    print("Candidato vencedor: THOR")
elif candidatos["Homem de Ferro"] >  candidatos["Thor"] and candidatos["Homem de Ferro"] > candidatos["Hulk"] and candidatos["Homem de Ferro"] > candidatos["Nulo"] and candidatos["Homem de Ferro"] > candidatos["Branco"]:
    print("Candidato vencedor: HOMEM DE FERRO")
elif candidatos["Hulk"] >  candidatos["Thor"] and candidatos["Homem de Ferro"] < candidatos["Hulk"] and candidatos["Hulk"] > candidatos["Nulo"] and candidatos["Hulk"] > candidatos["Branco"]:
    print("Candidato vencedor: HULK") 
elif candidatos["Nulo"] >  candidatos["Homem de Ferro"] and candidatos["Nulo"] > candidatos["Hulk"] and candidatos["Nulo"] > candidatos["Thor"] and candidatos["Nulo"] > candidatos["Branco"]:
    print("A maioria dos votos foi NULO")
elif candidatos["Branco"] >  candidatos["Homem de Ferro"] and candidatos["Branco"] > candidatos["Hulk"] and candidatos["Branco"] > candidatos["Thor"] and candidatos["Nulo"] < candidatos["Branco"]:
    print("A maioria dos votos foi BRANCO")

print()