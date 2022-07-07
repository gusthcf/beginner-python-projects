'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opcao = 1
while opcao != 5:
    print(f'''{'-='*20}
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {valor1} e {valor2} é {valor1+valor2}')
    elif opcao == 2:
        print(f'O resultado de {valor1} x {valor2} é {valor1*valor2}')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'Entre {valor1} e {valor2} o maior é {valor1}')
        elif valor2 > valor1:
            print(f'Entre {valor1} e {valor2} o maior é {valor2}')
        else:
            print('Os dois valores digitados são iguais.')
    elif opcao == 4:
        print('Informe os números novamente:')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao > 5 or opcao < 1:
        print('Opção inválida. Tente novamente.')
print('Finalizando...')
sleep(1)
print(f'''{'-='*20}
Fim do programa! Volte sempre''')