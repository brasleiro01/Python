# Operadore in e not in
# Strings são interáveis
#  0 1 2 3 4 5
#  M a r c u s
# -6-5-4-3-2-1

nome = 'Marcus'
print(nome[2])

print('p' in nome)
print('vi' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')