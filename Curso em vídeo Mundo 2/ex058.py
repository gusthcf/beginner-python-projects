'''
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
'''
from random import randint
print(''' Sou seu computador... 
Acabei de pensar em um número entre 0 e 10.
Consegue adivinhar qual foi?''')
pc = randint(0, 10)
palpite = int(input('Qual o seu palpite? '))
t = 1
while palpite < 0 or palpite > 10:
    palpite = int(input('\033[31mDigite um palpite válido.\033[m Qual o seu palpite? '))
while palpite != pc:
    if palpite > pc:
        palpite = int(input('Menos... tente mais uma vez. '))
    else:
        palpite = int(input('Mais... tente mais uma vez. '))
    t += 1
print(f'Você acertou com {t} tentativas! Parabéns!')