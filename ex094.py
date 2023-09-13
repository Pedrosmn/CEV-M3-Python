cadastrados = list()
pessoa = dict()
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo: [M/F] ')).split()[0]
    while pessoa['Sexo'] not in 'MFmf':
        pessoa['Sexo'] = str(input('Digite "M" ou "F": '))
    pessoa['Idade'] = int(input('Idade: '))
    cadastrados.append(pessoa.copy())
    continuidade = str(input('Quer continuar? [S/N] ')).split()[0]
    while continuidade not in 'SNsn':
        continuidade = str(input('Digite "S" para continuar "N" para parar. '))
    if continuidade in 'Nn':
        break
print('-'*30)
print(f'A) Ao todo temos {len(cadastrados)} pessoas cadastradas')
media = 0
for c in cadastrados:
    media += c['Idade']
media = media / len(cadastrados)
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for c in cadastrados:
    if c['Sexo'] in 'Ff':
        print(f'{c["Nome"]} ', end='')
print('\nD) Lista das pessoas que estão acima da média de idade: ')
for c in cadastrados:
    if c['Idade'] > media:
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
