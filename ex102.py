def fatorial(num=1, show=False):
    """
    Calcula o fatorial de um número
    n: número a ser calculado
    show: opcional. True mostra a conta, False não mostra
    return resultado da fatorial"""


    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(7, True))
print(help(fatorial))