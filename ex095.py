elenco = list()
jogador = dict()
print('SOFASCORE DE PARIPUEIRA')
while True:
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    total_gols = 0
    gols = list()
    jogador['Gols'] = gols
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
        total_gols += gols[c]
    jogador['Total'] = total_gols
    elenco.append(jogador.copy())
    continuidade = str(input('Quer continuar? [S/N]: ')).strip()[0]
    while continuidade not in 'SsNn':
        continuidade = str(input('Digite "Sim" ou "Não": ')).strip()[0]
    if continuidade in 'Nn':
        break
print('-'*50)
print('Cod ', end='')
for k in jogador.keys():
    print(f'{k:<20}', end='')
print()
for c, dicts in enumerate(elenco):
    print(f'{c:>3} ', end='')
    for v in dicts.values():
        print(f'{str(v):<20}', end='')
    print()
print('-'*50)
while True:
    dado_individual = int(input('Mostrar dados de qual jogador? (999 ENCERRA) '))
    print('-'*50)
    while (dado_individual >= len(elenco) or dado_individual < 0) and dado_individual != 999:
        dado_individual = int(input('Jogador NÃO encontrado, digite novamente (999 ENCERRA) '))
    if dado_individual != 999:
        print(f'Estatísticas de {elenco[dado_individual]["Nome"]}')
        for c in range(0, len(elenco[dado_individual]["Gols"])):
            print(f'No jogo {c+1} fez {elenco[dado_individual]["Gols"][c]} gols.')
        print('-'*50)
    else:
        print('ENCERRANDO')
        break
