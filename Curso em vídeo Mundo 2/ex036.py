'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = casa/(anos*12)
if parcela > salario*0.3:
    print(f'A prestação para pagar uma casa de R${casa:.2f} em {anos} anos será de R${parcela:.2f}.')
    print('Esse valor excede 30% do salário! Empréstimo NEGADO!')
else:
    print(f'A prestação para pagar uma casa de R${casa:.2f} em {anos} anos será de R${parcela:.2f}.')
    print('O empréstimo pode ser concedido!')