'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão: 1 para binário,2 para octal e 3 para hexadecimal.
'''
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções de conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
con = int(input('Sua opção: '))
if con == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}.')
    # colocamos o [2:] para retirar os dois primeiros termos, que estavam apenas indicando que o valor estava em binário.
elif con == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}.')
elif con == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}.')
else:
    print('Opção inválida! Escolha a opção 1, 2 ou 3!')