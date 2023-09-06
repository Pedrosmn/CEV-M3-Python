total = contador_mil = menor = cont = 0
barato = ' '
print('VENDA')
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    cont += 1
    continuidade = ' '
    while continuidade not in 'SN':
        continuidade = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    total += preço
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    if preço > 1000:
        contador_mil += 1
    if continuidade == 'N':
        break
print(f'Total da compra: R${total:.2f}')
print(f'Temos {contador_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato é {barato} e custa {menor}')