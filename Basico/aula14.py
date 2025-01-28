# if / elif       / else
# se / se não se  / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Voce saiu do sistema')
else:
    print(entrada, 'não é uma opção disponivel.')