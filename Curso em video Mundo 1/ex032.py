'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
Se a pessoa quiser analisar o ano atual ela deve digitar 0.
'''
from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano de {ano} é bissexto!')
        else:
            print(f'O ano de {ano} não é bissexto!')
    else:
        print(f'O ano de {ano} é bissexto!')
else:
    print(f'O ano de {ano} não é bissexto!')