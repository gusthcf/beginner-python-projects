'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''
num = int(input('Digite um número de 0 a 9999: '))
print(f'Analisando o número {num}')
aux = str(10000 + num)
print(f'Unidade: {aux[4]}')
print(f'Dezena: {aux[3]}')
print(f'Centena: {aux[2]}')
print(f'Milhar: {aux[1]}')