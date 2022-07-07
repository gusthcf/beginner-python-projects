"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas, o nome com todas as letras minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""
nome = str(input('Digite seu nome completo: ')).strip()
#usamos o .strip ali para eliminar qualquer espaço inútil inserido antes ou depois do nome
print(f'O nome em maiúsculo é:{nome.upper()}')
print(f'O nome em minúsculo é:{nome.lower()}')
print(f'O nome todo tem {len(nome)-nome.count(" ")} letras.')
print(f'O primeiro nome tem {nome.find(" ")} letras.')
#também poderíamos achar o primeiro nome da seguinte maneira:
#separando a string utilizando a função split
#usando a função len para achar o número de caracteres do primeiro termo da lista formada