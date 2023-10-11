def notas(*n, sit=False):
    """
    Funcão para avaliar as notas dos alunos.
    n: notas do aluno
    sit: OPCIONAL, indica a situação da média do aluno
    return: dicionário com informações da notas do aluno
    """
    avaliação_nota = dict()
    avaliação_nota['total'] = len(n)
    avaliação_nota['maior'] = max(n)
    avaliação_nota['menor'] = min(n)
    contador_media = 0
    for c in n:
        contador_media += c
    media = contador_media / len(n)
    avaliação_nota['média'] = media
    if sit:
        if media < 6:
            avaliação_nota['situação'] = 'RUIM'
        elif media >= 6 and media < 8:
            avaliação_nota['situação'] = 'RAZOÁVEL'
        else:
            avaliação_nota['situação'] = 'BOA'
    return avaliação_nota


resp = notas(5.5, 6, 9, sit=True)
print(resp)
help(notas)