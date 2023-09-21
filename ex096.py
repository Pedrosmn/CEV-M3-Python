def área(x, y):
    area_total = x * y
    print(f'A área de um terreno {x}x{y} é de {area_total}m².')


largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
área(largura, comprimento)