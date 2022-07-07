'''
Faça um programa que pergune a distancia de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''
km = float(input("Qual foi a distância da viagem? "))
if km <= 200:
    print(f"A passagem irá custar R${0.5*km:.2f}!")
else:
    print(f"A passagem irá custar R${0.45*km:.2f}!")