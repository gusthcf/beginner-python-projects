'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do
homem mais velho e quantas mulheres têm menos de 20 anos.
'''
soma = 0
maior_idade = 0
menor_de_20 = 0
for i in range (1, 5):
    print(f'----- {i}° PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().lower()
    soma += idade
    if sexo == 'm':
        if idade > maior_idade:
            maior_idade = idade
            velho = nome
    else:
        if idade < 20:
            menor_de_20 += 1
print(f'''A média de idade do grupo é de {soma/4:.1f} anos.
O homem mais velho tem {maior_idade} anos e se chama {velho}.
Ao todo são {menor_de_20} mulheres com menos de 20 anos.''')
