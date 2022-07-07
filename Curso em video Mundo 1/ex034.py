'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Qual é o salário do funcionário? '))
if salario > 1250:
    print(f'O aumento será de R${salario*0.1:.2f}!')
    print(f'O funcionário passa a ganhar R${salario*0.1+salario:.2f}!')
else:
    print(f'O aumento será de R${salario*0.15:.2f}!')
    print(f'O funcionário passa a ganhar R${salario * 0.15 + salario:.2f}!')