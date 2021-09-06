contatinhos = [("Ana", "12345-6789"),("Maria", "98765-4123"),("João", "65412-9873")]
print(type(contatinhos))
print(contatinhos)

dicontatinhos = dict(contatinhos)
print(dicontatinhos)
print(type(dicontatinhos))
print()
print(dicontatinhos["Maria"])
print()
print("=="*20)

vingadores = {"Chris Evans" : "Capitão América", "Mark Ruffalo":"Hulk", "Tom Hiddleston":"Loki", "Chris Hemworth":"Thor", "Robert Downey Jr":"Homem de Ferro", "Scarlett Johansson": "Viúva Negra"} 
print(vingadores)
print()
vingadores ["Homem Formiga"] = "Paul Rudd"
print(vingadores)
print()

#EXERCÍCIO 2
numerosquadrados = {}
listanum = [1,4,5,6,7,9]

for n in listanum:
    numerosquadrados [n] = n*n
    
print(numerosquadrados)
print()

#b - exerc 2

quadrados2 = {}

for n in range(1,11):
    quadrados2 [n] = n*n
print(quadrados2)    
print ()
numero = int(input("Entre com o número: "))
quadrados3 = {}
for n in range(1,numero+1):
    quadrados3 [n] = n*n
print (quadrados3)