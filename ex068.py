from random import randint

contador = 0
resultado = ''

print('JOGO DO PAR OU ÍMPAR')
while True:
    rand = randint(0, 10)
    decisão = str(input('Par ou Ímpar? (P/I) ')).upper()
    n = int(input('Diga um número: '))
    print(f'Você jogou {n} e o computador jogou {rand}, TOTAL = {n + rand}')
    if ((n + rand) % 2 == 0 and decisão == 'P') or ((n + rand) % 2 != 0 and decisão == 'I'):
        print('VENCEU, JOGUE NOVAMENTE')
        print('-'*50)
        contador += 1
    else:
        print('-'*50)
        print(f'PERDEU!! Você ganhou {contador}x')
        break