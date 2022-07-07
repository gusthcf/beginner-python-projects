co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
from math import hypot
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}.')