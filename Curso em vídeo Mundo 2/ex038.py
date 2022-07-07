'''
Escreva um programa que leia dois números inteiros e compare-os.
'''
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
if num1 > num2:
    print(f'O número {num1} é maior.')
elif num2 > num1:
    print(f'O número {num2} é maior.')
else:
    print(f'Não existe valor maior! Os dois números são iguais!')