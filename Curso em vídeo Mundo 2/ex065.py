'''Crie um programa que leia vários números inteiros pelo teclado.No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
num = int(input('Digite um número: '))
opcao = input('Quer continuar? (S/N): ').strip().lower()[0]
maior = menor = soma =num
cont = 1
while opcao == 's':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    opcao = input('Quer continuar? (S/N): ').strip().lower()[0]
print(f'Você digitou {cont} números e a média foi {soma/cont:.1f}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}.')

