'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
maiores = 0
menores = 0
for i in range (1, 8):
    ano = int(input(f'Em que ano a {i}° pessoa nasceu? '))
    if date.today().year - ano > 18:
        maiores += 1
    else:
        menores += 1
print(f'Ao todo tivemos {maiores} pessoa(s) maior(es) de idade e {menores} menor(es) de idade.')