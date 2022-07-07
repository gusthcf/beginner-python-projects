# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Qual o seu nome completo? ')).lower().strip().split()
print(f'Seu nome possui "SILVA"? {"silva" in nome}')