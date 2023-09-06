contador_50 = contador_20 = contador_10 = contador_1 = 0
print('CAIXA ELETRÔNICO')
valor = int(input('Qual valor você deseja sacar? '))
while valor >= 50:
    valor -= 50
    contador_50 += 1
while valor >= 20:
    valor -= 20
    contador_20 += 1
while valor >= 10:
    valor -= 10
    contador_10 += 1
while valor >= 1:
    valor -= 1
    contador_1 += 1
print(f'{contador_50} {contador_20} {contador_10} {contador_1}')