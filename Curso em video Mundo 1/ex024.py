#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
city = str(input('Em qual cidade você nasceu? ')).lower().strip().split()
print(f'{"santo" in city[0]}')