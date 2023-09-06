lista = []
lista_par = []
lista_impar = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? (S/N) ')).split()[0]
    if continuar == 'N':
        for c in lista:
            if c % 2 == 0:
                lista_par.append(c)
            else:
                lista_impar.append(c)
        print(f'Lista completa {lista}')
        print(f'Lista dos Pares {lista_par}')
        print(f'Lista dos Ímpares {lista_impar}')
        break
    