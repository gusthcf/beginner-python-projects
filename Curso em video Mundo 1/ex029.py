'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80/Km ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''
vel = float(input("A que velocidade o carro está? "))
if vel > 80:
    print("Você está acima da velocidade permitida que é de 80 Km/h!")
    print(f"Você deverá pagar uma multa de R${(vel-80)*7:.2f}!")
print("Tenha um bom dia! Dirija com segurança!")