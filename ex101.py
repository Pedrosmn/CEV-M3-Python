def voto(ano):
    from datetime import date
    global idade
    idade = date.today().year - ano
    if idade < 16:
        return 'Voto NEGADO'
    elif (idade >= 16 and idade < 18) or idade >= 65:
        return 'Voto OPCIONAL'
    else:
        return 'Voto OBRIGATÓRIO'


ano_nascimento = int(input('Qual ano você nasceu? '))
resultado = voto(ano_nascimento)
print(f'Com {idade}. {resultado}')
