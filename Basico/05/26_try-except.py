"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# print(12345)
# print(456)
# int('a')

numero_str = input('vou dobrar o numero que você digitar: ')

try:
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')