# Faça um programa com uma função chamada somaImposto. 
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.


def somaImposto(taxaImposto,custo):
    valorComImposto = (custo * (taxaImposto/100)) + custo
    return valorComImposto

taxa = float(input('Digite a taxa de imposto: ').replace(',','.'))
custo = float(input('Digite o valor do produto: R$ ').replace(',','.'))

print(f'O valor do produto com imposto será de R$ {somaImposto(taxa,custo):.2f}')
