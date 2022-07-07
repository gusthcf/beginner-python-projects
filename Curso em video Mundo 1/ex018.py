ang = float(input('Digite um ângulo: '))
from math import radians, sin, cos, tan
# usamos o radians porque as funções sin, cos e tan só aceitam o ângulo em radianos.
# por isso convertemos o ãngulo para radianos ao aplicarmos essas funções.
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'O ângulo de {ang} tem o seno de {seno:.2f}')
print(f'O ângulo de {ang} tem o cosseno de {cos:.2f}')
print(f'O ângulo de {ang} tem a tangente de {tan:.2f}')