'''
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
print('''\033[1;33mCALCULADORA DE TABUADA!\033[m
Instruções: para parar a calculadora, basta digitar um valor negativo como entrada.''')
while True:
    print('=' * 40)
    n = int(input('Quer ver a tabuada de qual número, amigo? '))
    print('='*40)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i:2d} = {n*i}')
print('\033[32mPrograma de tabuada encerrado! Volte sempre!\033[m')