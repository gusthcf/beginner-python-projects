print(f'\033[1;32;40mExemplo 1\033[m')
a = 2
b = 5
print(f'Os valores são \033[1;32m{a}\033[m e \033[1;32m{b}\033[m!!!')
# repare que o \033[m deve vir no início e onde vc quer que terminem as cores
print(f'\033[1;32;40mExemplo 2\033[m')
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print(f"Os valores são {cores['azul']}{a}{cores['limpa']} e {cores['amarelo']}{b}{cores['limpa']}! ")
# aqui mostramos que também é possível organizar as cores em listas para facilitar.