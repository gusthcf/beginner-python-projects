'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
print('\033[1;33mCalculando 10 termos de uma PA\033[m')
inicio = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
decimo = inicio+(razao*9)
for i in range(inicio, decimo+razao, razao):
    print(f'{i}', end=' ➔ ')
print('ACABOU!')