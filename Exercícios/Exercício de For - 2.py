#Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores

print("=="*20)
print("               Divisores               ")
print("=="*20)
print()
n = int(input("Informe o valor para descobir seus divisores: "))
for i in range(1,n): #a varíavel 'i' vai percorrer de 1 a n. 
    if n % i == 0:  #se o input da variavel 'n' for divisivel por 'i' com resto 0, printa o valor de i
        print(i) #i é o valor de cada variável de 1 a n
        