idade = -1
sexo = 'p'
continuidade = 'p'
contador_18 = 0
contador_20 = 0
contador_mulher = 0
contador_homem = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('-'*50)
    while idade < 0:
        idade = int(input('Idade: '))
        if idade >= 18:
            contador_18 += 1
        elif idade < 20:
            contador_20 += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M] ')).upper()
        if sexo == 'F':
            contador_mulher += 1
        elif sexo == 'M':
            contador_homem += 1
    while continuidade not in 'SN':
        continuidade = str(input('Quer continuar? [S/N] ')).upper()
    if continuidade == 'N':
        print('-'*50)
        print(f'Total de pessoas com mais de 18 anos: {contador_18}')
        print(f'Ao todo temos {contador_homem} homens cadastrados')
        print(f'E temos {contador_20} mulheres com menos de 20 anos')
        break
    else:
        print('-'*50)
        idade = -1
        sexo = 'p'
        continuidade = 'p'