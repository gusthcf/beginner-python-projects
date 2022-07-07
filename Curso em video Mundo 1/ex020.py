a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
from random import sample
lista = [a1, a2, a3, a4]
lista = sample(lista, k=4)
print('A ordem de apresentação será:')
print(f'{lista}')