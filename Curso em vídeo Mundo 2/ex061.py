'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma
PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
print('Gerador de PA')
p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
while c < 10:
    print(f'{p1} > ', end='')
    p1 += r
    c += 1
print('FIM')
