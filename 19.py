def funcao(valor):
    notas_de_100 = int(valor // 100)
    notas_de_50 = int((valor % 100) // 50)
    notas_de_20 = int(((valor % 100) % 50) // 20)
    notas_de_10 = int((((valor % 100) % 50) % 20) // 10)
    notas_de_5 = int(((((valor % 100) % 50) % 20) % 10) // 5)
    notas_de_2 = int((((((valor % 100) % 50) % 20) % 10) % 5) // 2)
    notas_de_1 = int(((((((valor % 100) % 50) % 20) % 10) % 5) % 2) // 1)
    return notas_de_100, notas_de_50, notas_de_20, notas_de_10, notas_de_5, notas_de_2, notas_de_1
