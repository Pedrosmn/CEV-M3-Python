from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram {numeros}')
print(f'O maior número é o {sorted(numeros)[4]}')
print(f'O menor número é o {sorted(numeros)[0]}')