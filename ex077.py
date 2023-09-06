palavras = ('teste', 'almoço', 'palheta', 'mouse', 'bola', 'rede')
for c in palavras:
    print(f'Na palavra {c.upper()} temos ', end='')
    for i in c:
        if i in 'aeiou':
            print(f'{i} ', end='')
    print('')