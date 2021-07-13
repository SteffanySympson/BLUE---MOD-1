# 4.	Faça um programa que calcule o salário de um colaborador na empresa XYZ.
# O salário é pago conforme a quantidade de horas trabalhadas.
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def salario(valorHora,tempo):
    if tempo <= 40:
        salario = valorHora * tempo
        return salario
    elif tempo > 40:
       salario =  (valorHora + (valorHora * 1.5/100)) * tempo
       return salario

valorHora = float(input('Informe o valor por hora trabalhada: R$'))
tempo = int(input('Informe quantas horas o colaborador trabalhou: '))
print()
print(f'O salario será R$ {salario(valorHora,tempo):.2f}')
