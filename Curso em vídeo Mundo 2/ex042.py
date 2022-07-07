'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
'''
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a+b > c and b+c > a and c+a > b:
    if a == b == c:
        trian = 'EQUILÁTERO'
    elif a!= b != c != a:
        trian = 'ESCALENO'
    else:
        trian = 'ISÓSCELES'
    print(f'Os seguimentos acima \33[1;32mPODEM\33[m formar um triângulo \33[1;34m{trian}\33[m!')
else:
    print('Os seguimentos acima \33[1;31mNÃO PODEM\33[m formar um triângulo!')
