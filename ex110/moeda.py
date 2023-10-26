def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def metade(n, formatar = False):
    n = n / 2
    if formatar:
        n = moeda(n)
    return n


def dobro(n, formatar = False):
    n = n * 2
    if formatar:
        n = moeda(n)
    return n


def aumentar(n, taxa, formatar = False):
    n = (n * taxa/100) + n
    if formatar:
        n = moeda(n)
    return n


def reduzir(n, taxa, formatar = False):
    n = n - (n * taxa/100)
    if formatar:
        n = moeda(n)
    return n

def resumo(preço=0, aumento=0, redução=0):
    print('-'*30)
    print('RESUMO DO VALOR'. center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    if aumento > 0:
        print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    if redução > 0:
        print(f'{redução}% de redução: \t{reduzir(preço, redução, True    )}')
    print('-'*30)
    