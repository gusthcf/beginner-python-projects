'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
print('\033[1;36mPAR OU ÍMPAR!!!\033[m')
vit = 0
while True:
    print('==='*10)
    n = int(input('Diga um valor: '))
    opcao = input('Par ou ímpar? [P/I]? ').strip().lower()[0]
    print('---'*17)
    pc = randint(0, 10)
    total = n+pc
    print(f'Você jogou {n} e o computador {pc}. Total de {total}. ', end='')
    print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')
    if total % 2 == 0 and opcao == 'p':
        print('VOCÊ VENCEU! Vamos jogar novamente...')
        vit += 1
    elif total % 2 != 0 and opcao == 'i':
        print('VOCÊ VENCEU! Vamos jogar novamente...')
        vit += 1
    elif total % 2 == 0:
        break
    else:
        break
print('VOCÊ PERDEU!')
print('==='*20)
print(f'GAME OVER! Você venceu {vit} vezes.')

