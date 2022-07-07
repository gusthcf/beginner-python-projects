'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto – em até 2x no cartão: preço formal – 3x ou mais no cartão: 20% de juros
'''
preco = float(input('Preço das compras: R$'))
print('''\033[1;4;34mFormas de pagamento\033[m:
\033[1;34m[ 1 ]\033[m à vista dinheiro/cheque
\033[1;34m[ 2 ]\033[m à vista cartão
\033[1;34m[ 3 ]\033[m 2x no cartão
\033[1;34m[ 4 ]\033[m 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if 1 <= opcao <=4:
    if opcao == 1:
        preco2 = preco-(preco*0.1)
    elif opcao == 2:
        preco2 = preco-(preco*0.05)
    elif opcao == 3:
        preco2 = preco
        print(f'\033[1;32mSua compra será parcelada em 2x de R${preco/2:.2f}!\033[m')
    else:
        parcelas = int(input('Quantas parcelas? '))
        preco2 = preco+(preco*0.2)
        print(f'\033[1;32mSua compra será parcelada em {parcelas}x de R${preco2/parcelas:.2f} com juros!\033[m')
    print(f'\033[1;32mSua compra de R${preco:.2f} vai custar R${preco2:.2f} no final.\033[m')
else:
    print('\033[1;31mEscolha uma opção de 1 a 4!\033[m')
