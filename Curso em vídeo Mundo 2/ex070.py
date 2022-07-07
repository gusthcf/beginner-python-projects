'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se
o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.
'''
print('\033[1;33mLOJA GUSTAVINHO COMPRAS\033[m')
total = totmil = cont = menor = 0
barato = ''
while True:
    produto = input('Nome do produto: ').strip()
    preco = int(input('Preço do produto: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    opcao = ' '
    while opcao not in 'sn':
        opcao = input('Quer continuar? (S/N) ').strip().lower()
    if opcao == 'n':
        break
print(f'''\033[1;33mDados:\033[m
O total da compra foi de \033[1;33mR${total:.2f}\033[m.
Há \033[1;34m{totmil}\033[m produtos custando mais de R$1000.00.
O produto mais barato foi \033[1;34m{barato}\033[m e custou Há \033[1;34mR${menor:.2f}\033[m.''')
