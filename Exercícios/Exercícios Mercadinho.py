### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

#Criar um estoque com item e quantidade de cada item 
#Se não tiver o produto na lista retornar prduto inválido
#se estoque zerado retornar produto indisponivel
#se quantidade solicitada maior que quantidade em estoque informar quantidade indisponivel

# produtos = {"Batata":"20", "Miojo":"50", "Coca":"120", "Palito de chocolate":"60","Nuggets":"100", "Geleia":"15"}
# print (produtos)


total = mais1000 = mais_barato = unidade = 0
nome = ''
while True:
    produto = input('Produto: ').strip()
    preco = float(input('Preço do produto: R$ ').replace(',','.'))
    unidade += 1
    total += preco
    if preco > 1000:
        mais1000 += 1
    if unidade == 1:
        mais_barato = preco
        nome = produto
    else:
        if preco < mais_barato:
            mais_barato = preco
            nome = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').upper().strip()
    if continuar == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Quantidade de produtos que custam mais de R$ 1000.00: {mais1000}')
print(f'O produto mais barato é: {nome}')

######

total = mais1000 = mais_barato = unidade = 0
nome = ''
while True:
    produto = input('Produto: ').strip()
    preco = float(input('Preço do produto: R$ ').replace(',','.'))
    unidade += 1
    total += preco
    if preco > 1000:
        mais1000 += 1
    if unidade == 1:
        mais_barato = preco
        nome = produto
    else:
        if preco < mais_barato:
            mais_barato = preco
            nome = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').upper().strip()
    if continuar == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Quantidade de produtos que custam mais de R$ 1000.00: {mais1000}')
print(f'O produto mais barato é: {nome}')
elif produto not in estoque.keys():
        print('Produto Inválido')
print()
total_compras = 0
for i in dic_produtosComprados:
     print(f'Você comprou {dic_produtosComprados[i][0]} unidades de {i} e custou R$ {dic_produtosComprados[i][1]:.2f}')
     total_compras += dic_produtosComprados[i][1]
print(f'O total de suas compras deu R$ {total_compras:.2f}')
