'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
num = int(input('Digite um número: '))
divisoes = 0
for i in range(1, num+1):
    if num % i == 0:
        print(f'\033[1;32m{i}\033[m', end=' ')
        divisoes += 1
    else:
        print(f'\033[1;31m{i}\033[m', end=' ')
if divisoes == 2:
    primo = 'É PRIMO!'
else:
    primo = 'NÃO É PRIMO!'
print(f'''\nO número {num} foi divisível {divisoes} vezes.
E por isso, ele {primo}''')
