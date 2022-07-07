'''
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
'''
num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    # aqui pegamos o resto da divisão do número por 2, se for 0 o número é par
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é impar!")