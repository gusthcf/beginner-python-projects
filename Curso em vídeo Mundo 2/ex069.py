'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.
'''
c = homem = muie = 0
while True:
    print('\033[1;33mCADASTRE UMA PESSOA\033[m')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = input('Sexo (M/F): ').strip().lower()[0]
    if idade > 18:
        c += 1
    if sexo == 'm':
        homem += 1
    elif sexo == 'f':
        if idade < 20:
            muie += 1
    opcao = ' '
    while opcao not in 'sn':
         opcao = input('Quer continuar? (S/N) ').strip().lower()[0]
    if opcao == 'n':
        break
print(f'''\033[1;33mDados:\033[m 
\033[1;34m{c}\033[m pessoas cadastradas tem mais de 18 anos.
\033[1;34m{homem}\033[m homem(s) foram cadastrado(s).
\033[1;34m{muie}\033[m mulher(es) tem menos de 20 anos.''')