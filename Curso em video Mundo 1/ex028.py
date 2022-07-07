'''
Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deve escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
#vamos usar a função sleep da biblioteca time para dar uma animação como se o computador estivesse dormindo....
print("Pensarei em um número entre 0 e 5... tente adivinhar qual foi!")
num = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(2)
#faz com que o programa pare por 3 segundos
computador = randint(0,5)
if num == computador:
    print("Maldito! Você advinhou o número que pensei!")
else:
    print("Ganhei otário! Você não advinhou meu número...")


