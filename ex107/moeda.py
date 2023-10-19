def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def metade(n):
    n = n / 2
    return moeda(n)


def dobro(n):
    n = n * 2
    return moeda(n)


def aumentar(n, taxa):
    n = (n * taxa/100) + n
    return moeda(n)
