from time import sleep
def contador(inicio, fim, razão):
    print('-'*30)
    print(f'Contagem de {inicio} até {fim} de {razão} em {razão}')
    i = inicio
    while True:
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
        if razão < 0:
            razão = razão * -1
        if fim < inicio:
            i -= razão
            if i < fim:
                print()
                break
        elif inicio < fim:
            i += razão
            if i > fim:
                print()
                break


contador(10, 0, 2)
contador(0, 10, 2)
print('-'*30)
print('Escolha a sua contagem')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
razão = int(input('Razão: '))
contador(inicio, fim, razão)