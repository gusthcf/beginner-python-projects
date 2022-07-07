dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados? '))
preco = dias*60 + km*0.15
print(f'O preço total a se pagar é de R${preco:.2f}.')