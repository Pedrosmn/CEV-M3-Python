auxiliar = n = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    while auxiliar < 11:
        print(f'{n} x {auxiliar} = {n * auxiliar}')
        auxiliar += 1
        if auxiliar == 11:
            auxiliar = 1
            break
print(f'Programa finalizado!!')