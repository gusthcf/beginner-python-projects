'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
maior = 0
menor = 9999
for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'''O menor peso lido foi {menor:.1f} Kg.
O maior peso lido foi {maior:.1f} Kg.''')