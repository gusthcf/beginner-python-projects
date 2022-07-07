preco = float(input('Digite o preço do produto: '))
desconto = preco - (preco*0.05)
print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${desconto:.2f}.')