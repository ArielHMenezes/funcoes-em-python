def funcao(segundo):
    hora = int(segundo//3600)
    segundo = int(segundo%3600)
    minuto = int(segundo//60)
    segundo = int(segundo%60)
    return hora, minuto, segundo