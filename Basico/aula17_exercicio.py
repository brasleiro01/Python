primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro = int(primeiro_valor)
segundo = int(segundo_valor)

if primeiro > segundo:
    print(f'{primeiro=} é maior ou igual ao segundo')
else:
    print(f'{segundo=} é maior ou igual ao primeiro')