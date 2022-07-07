'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'Você nasceu em {ano} tem {idade} anos em {atual}.')
if idade < 18:
    print(f'Ainda faltam {18-idade} anos para o alistamento')
    print(f'Seu alistamento será em {atual+(18-idade)}.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade-18} anos.')
    print(f'Seu alistamento foi em {atual-(idade-18)}.')
else:
    print(f'Você tem que se alistar esse ano!!!')