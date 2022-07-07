'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade: – Até 9 anos: MIRIM – Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR – Até 25 anos: SÊNIOR – Acima de 25 anos: MASTER
'''
from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    cat = 'MIRIM'
elif idade <= 14:
    cat = 'INFANTIL'
elif idade <= 19:
    cat = 'JÚNIOR'
elif idade <= 25:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'
print(f'Classificação: \33[1;34m{cat}\33[m')