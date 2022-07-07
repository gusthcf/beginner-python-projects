'''
Melhore o DESAFIO 61, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
print('Gerador de PA')
p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
contador = 0
termos = 10
while termos != 0:
    c = 0
    while c < termos:
        print(f'{p1} > ', end='')
        p1 += r
        c += 1
        contador += 1
    print('PAUSA')
    termos = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {contador} termos.')



