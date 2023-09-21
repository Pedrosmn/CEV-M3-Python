from time import sleep 
def maior(*num):
    print('-'*30)
    cont = maior = 0
    for c in num:
        print(f'{c} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    print(f'\nTemos {cont} números na lista')
    print(f'O maior é {maior}')


maior(2, 4, 1, 80, 5, 0)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
