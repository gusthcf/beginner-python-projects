'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import choice
from time import sleep
print('''\033[1;30;43mJokenpô\033[m
[ 1 ] \033[1;33m✊\033[m PEDRA 
[ 2 ] \033[1;33m🖐\033[m PAPEL
[ 3 ] \033[1;33m✌\033[m TESOURA''')
opcao = int(input('Qual você vai jogar? '))
pc = choice([1, 2, 3])
textos = ['\033[1;32m✊ PEDRA\033[m', '\033[1;32m🖐 PAPEL\033[m', '\033[1;32m✌ TESOURA\033[m']
resultados = ['\033[1;32mVOCÊ VENCEU!\033[m', '\033[1;34mEMPATE!\033[m', '\033[1;31mVOCÊ PERDEU!\033[m']
if 1 <= opcao <= 3:
    if pc == opcao:
        resul = resultados[1]
    elif pc == 1:
        if opcao == 2:
            resul = resultados[0]
        else:
            resul = resultados[2]
    elif pc == 2:
        if opcao == 1:
            resul = resultados[2]
        else:
            resul = resultados[0]
    elif pc == 3:
        if opcao == 1:
            resul = resultados[0]
        else:
            resul = resultados[2]
    print('\033[1;33mJÔ\033[m')
    sleep(0.5)
    print('\033[1;33mKEN\033[m')
    sleep(0.5)
    print('\033[1;33mPO!!!\033[m')
    sleep(0.5)
    print(f'Você jogou {textos[opcao-1]}!')
    print(f'O computador jogou {textos[pc-1]}!')
    print(f'{resul}')
else:
    print(f'\033[1;31mEscolha uma opção válida!!!\033[m')
