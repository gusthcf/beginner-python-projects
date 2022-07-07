'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
print('\033[1;34mBANCO CENTRAL GUGU DA BIKE\033[m')
valor = int(input('Qual valor você quer sacar? R$'))
lista = [50, 20, 10, 1]
for i in range(0, 4):
    if valor >= lista[i]:
        print(f'Total de {valor//lista[i]} cédulas de R${lista[i]:.2f}')
        valor = valor % lista[i]
