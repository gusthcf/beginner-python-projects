'''Faça um programa que leia um número qualquer e mostre o seu fatorial'''
from math import factorial
print('MODO 1 - MAIS FÁCIL')
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')
print('###'*10)
print('MODO 2 - TRADICIONAL')
n = int(input('Digite um número para calcular seu fatorial: '))
c = n-1
f = n
print(f'Calculando {n}! = {n}', end='')
while c != 0:
    print(f' x {c}', end='')
    f *= c
    c -= 1
print(f' = {f}')