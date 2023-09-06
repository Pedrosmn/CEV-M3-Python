geral = list()
par = list()
impar = list()
for c in range(7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
geral.append(impar[:])
geral.append(par[:])

print(sorted(par))
print(sorted(impar))
print(geral)