# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('senha: ')

if not senha != '123456':
    print('Senha incorreta.')

print(not True)
print(not False)