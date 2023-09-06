pessoas = list()
maior = menor = 0
while True:
    temp = list()
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if maior < temp[1]:
            maior = temp[1]
        if menor > temp[1]:
            menor = temp[1]
    pessoas.append(temp)
    continuar = str(input('Quer continuar? (S/N) ')).upper().split()[0]
    if continuar in 'N':
        print(f'{len(pessoas)} Cadastradas na lista.')
        print(f'O Maior peso foi de {maior}Kg. Peso de ', end='')
        for p in pessoas:
            if p[1] == maior:
                print(f'[{p[0]}] ', end='')
        print(f'\nO Menor peso foi de {menor}Kg. Peso de ', end='')
        for p in pessoas:
            if p[1] == menor:
                print(f'[{p[0]}] ', end='')
        break
#Copiado