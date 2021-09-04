from random import randint

n = int (randint(10,20)) #tamanho do array Pontuação (número de colaboradores participantes) sorteado com o liminte mínimo de 5 posições e no máximo 20, sendo sempre inteiros

def sorteia(lista):
    for cont in range(0,n):
        lista.append(randint(1,109)) #limitação da pontuação dada pelo enunciado, sendo 1 a menor pontuação permitida e 109 a maior.

pontuacao = [] #Lista de pontuações dos colaboradores
sorteia(pontuacao) #lista de pontuações sorteada

print (f'A lista de pontuação dos colaboradores é: {pontuacao}') #Exibição da lista de pontuação dos colaboradores
print()
print(f'Temos {n} colaboradores participando da nossa seleção para o time!')

tamanho_do_time = int(randint(3,9)) #um time é formado a partir de 3 participantes, este é limitado a um posição a menos que o menor número possível de colaboradores participantes definido no randint da variável N
print()
print (f'O time será formado por {tamanho_do_time} posições.') 
print()

time = []
k = 3 #a seleção será dos 3 primeiros itens da lista pontuação
while len(time) < tamanho_do_time:
    fatiamento_k = (pontuacao[0:3]) #fatiamento das 3 primeiras posições da lista Pontuação
    print(f'O conjunto para seleção do time é: {fatiamento_k}')
    maior_fatiamento = max(fatiamento_k) #maior número que veio do fatiamento
    print(f'A maior posição do conjunto é: {maior_fatiamento}')
    time.append(maior_fatiamento)
    pontuacao.remove(maior_fatiamento)
    print(f'A nova lista de pontuações é: {pontuacao} ')

print()
print(f'Nosso time final é: {time}')
soma=sum(time)
print()
print(f'A soma das pontuações do nosso time final é: {soma}')