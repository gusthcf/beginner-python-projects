'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:– Média abaixo de 5.0: REPROVADO; – Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
'''
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1+nota2)/2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}!')
if media < 5:
    print('O aluno está \033[1;31mREPROVADO\033[m!')
elif 5 <= media <= 6.9:
    print('O aluno está em \033[1;31mRECUPERAÇÃO\033[m!')
else:
    print('O aluno foi \033[1;32mAPROVADO\033[m!')