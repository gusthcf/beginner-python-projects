'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
a = float(input('Primeiro seguimento: '))
b = float(input('Segundo seguimento: '))
c = float(input('Terceiro seguimento: '))
if a+b > c and b+c > a and c+a > b:
    print('Os seguimentos acima PODEM formar um triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo!')