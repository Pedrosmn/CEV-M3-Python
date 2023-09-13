jogador = dict()
gols = list()
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
total_gols = 0
jogador['Gols'] = gols
for c in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    total_gols += gols[c]
jogador['Total'] = total_gols
print('-'*25)
print(jogador)
print('-'*25)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*25)
for c in range(partidas):
    print(f'Na partida {c+1}, fez {gols[c]} gols.')
