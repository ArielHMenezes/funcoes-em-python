def funcao(num):
    centena = num // 100
    dezena = (num % 100) // 10
    unidade = (num % 100) % 10
    newnum = unidade * 100 + dezena * 10 + centena
    return newnum