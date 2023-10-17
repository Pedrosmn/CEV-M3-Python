while True:
    print('-'*30)
    cmd = str(input('Digite a função ou biblioteca: ')).lower().strip()
    if cmd == 'fim':
        print('Finalizando o programa.')
        break
    print('-'*30)
    print(help(cmd))