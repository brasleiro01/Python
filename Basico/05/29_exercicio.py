"""
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuário não digite um numero inteiro,
informe que não é um numero inteiro.
"""

entrada = input('informe um numero: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_res = 'impar'

    if par_impar:
        par_impar_res = 'par'

    print(f'O númerop {entrada_int} é {par_impar_res}')
else:
    print('Você não digitou um número inteiro')
