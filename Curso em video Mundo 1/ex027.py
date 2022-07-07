"""Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente."""
nome = input("Digite seu nome completo: ").strip().split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[-1]}')
#aqui, utilizamos o -1 para se referir ao último termo da lista
#se quisessemos o penúltimo, utilizaríamos o -2
