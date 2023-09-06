dic = dict()

dic['nome'] = str(input('Nome: '))
dic['media'] = float(input(f'Média de {dic["nome"]}: '))
if dic['media'] < 6:
    dic['situação'] = 'Reprovado'
else:
    dic['situação'] = 'Aprovado'
for k, v in dic.items():
    print(f'{k} é igual a {v}')