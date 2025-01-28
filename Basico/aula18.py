# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
# São considerados falsy (que você ja viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

# 1-exemplo
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if condição = True:
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# 2-exemplo
print(True and False and True) # sempre vai parar no false
print(True and 0 and True) # sempre vai parar no 0