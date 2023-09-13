from datetime import datetime
form = dict()
form['Nome'] = str(input('Nome: '))
form['Idade'] = (datetime.now().year - int(input('Ano de nascimento: ')))
form['CTPS'] = int(input('Carteira de trabalho (0 caso não tenha) '))
if form['CTPS'] != 0:
    form['Contratação'] = int(input('Ano de contratação: '))
    form['Salário'] = float(input('Salário: '))
print('-'*20)
for k, v in form.items():
    print(f'{k} tem o valor {v}')