# Data com mês por extenso. 
# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string 
# no formato D de mesPorExtenso de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
# Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto,
# sendo que nesses casos Fevereiro terá 29 dias.

# DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.

# meses = {"01":"Janeiro", "02": "Fevereiro", "03":"Março", "04":"Abril", "05":"Maio", "06":"Junho", "07":"Julho", "08":"Agosto", "09":"Setembro", "10":"Outubro","11":"Novembro","12":"Dezembro"}
# m = input("Digite o mês")
# for m in meses.values():
#     print(m)

from datetime import datetime #modulo para manipulação de data e hora
import locale #internacionalização do Python. Converte datas, valores e etc para o país/idioma indicado 
from time import sleep
locale.setlocale(locale.LC_ALL, 'pt_BR') # parte que define a localidade para a configuração padrão do usuário no código em q está sendo chamada

print ("="*30)
print ("          Date Convert")
print("="*30)
print()
sleep(0.5)
print ("Vamos realizar uma conversão de data?")
sleep(1)
print("...3")
sleep(0.5)
print("...2")
sleep(0.5)
print("...1")
sleep(0.5)
 
def retorna_data_extenso (data): 
    try:
        data_convertida = datetime.strptime(data, '%d/%m/%Y') #strptime = Analisa uma string em um objeto com um formato correspondente (datetime) ==> strptime(date_string, format) . strftime / Converte o objeto em uma string de acordo com um determinado formato. 
        dia = datetime.strftime(data_convertida, '%d')
        mes = datetime.strftime(data_convertida, '%B')
        ano = datetime.strftime(data_convertida, '%Y')
        return dia + " de " + mes.capitalize() + " de " + ano #concatenação das variáveis 
    except ValueError:
        if len(data.split('/')) == 3 and data.split('/')[0] == '29' and (data.split('/')[1] == '02' or data.split('/')[1] == '2'):
            print('Não será convertido porque não foi ano bissexto')
        else:
            print("Formato de data inválido. Insira a data no formato DD/MM/AAAA.")
        return None

while True:
    data = input("Digite a data no formato DD/MM/AAAA: ")
    data_por_extenso = retorna_data_extenso(data)

    if data_por_extenso is not None:
        print(data_por_extenso)
    continuar = str(input('Deseja continuar? [S/N] ').upper().strip()[0])
    while continuar not in 'SN':
            continuar = str(input('Deseja continuar? [S/N] ').upper().strip()[0])
    if continuar == 'N':
        break