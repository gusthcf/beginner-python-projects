'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
N primeiros elementos de uma Sequência de Fibonacci.
'''
print('Sequência de Fibonacci')
t = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
if t == 1:
    print(f'{t1} ', end='')
elif t == 2:
    print(f'{t1} > {t2} ', end='')
else:
    print(f'{t1} > {t2} ', end='')
    i = 0
    while i < t-2:
        atual = t1+t2
        print(f'> {atual} ', end='')
        t1 = t2
        t2 = atual
        i += 1
print('> FIM')


