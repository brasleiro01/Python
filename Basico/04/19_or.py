# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão inteira sera avaliada naquele valor.
# São considerados falsy (que você ja viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

# 1-exemplo
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if condição = True:
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# 2-exemplo (avaliação de curto circuito)
print(True or False) # sempre vai ser true
print(0 or False or 0 or 'abc') # sempre vai ser true
senha = input('senha: ') or 'Sem senha'
print(senha)