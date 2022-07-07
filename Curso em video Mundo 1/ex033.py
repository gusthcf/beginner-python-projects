'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
numeros = [a, b, c]
print(f"O maior valor digitado foi {max(numeros)}.")
print(f"O menor valor digitado foi {min(numeros)}.")
