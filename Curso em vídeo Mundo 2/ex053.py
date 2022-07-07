'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
EXEMPLOS: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO
'''
frase = input('Digite uma frase: ').strip().lower().replace(' ', '')
contrario = frase[::-1]
# aqui se você colocar só o -1 como sendo o passo, o python já considera que você quer pegar a frase invertida
print(f'O inverso de {frase} é {contrario}')
if frase == contrario:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

