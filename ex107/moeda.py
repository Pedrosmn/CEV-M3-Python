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
