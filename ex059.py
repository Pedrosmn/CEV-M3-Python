print('Fatorial')
n = int(input('Digite um número: '))
fat = n
while n >= 2:
    fat = fat * (n - 1)
    n -= 1
print('Fatorial é {}'.format(fat))