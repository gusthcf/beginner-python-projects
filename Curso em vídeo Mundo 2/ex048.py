'''
Faça um programa que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
soma = 0
num = 0
for i in range(3, 501, 6):
    soma = soma + i
    num = num + 1
print(f'A soma entre todos os {num} números é {soma}')
