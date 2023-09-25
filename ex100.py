from time import sleep
from random import randint

def sorteia(lista):
    print('Sorteando 5 valores aleatórios: ', end='')
    for c in range(5):
        sorteado = randint(0, 9)
        print(f'{sorteado} ', end='', flush=True)
        sleep(0.5)
        lista.append(sorteado)

        
def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'\nA soma dos valore PARES é {soma}.')


números = list()
sorteia(números)
somaPar(números)
