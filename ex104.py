def leiaInt(pergunta):
    valor = str(input(pergunta))
    if valor.isnumeric():
        return valor
    while valor.isalpha() or valor.strip() == '':
        print('\033[31mERRO\033[0;0m')
        valor = str(input(pergunta))
    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
