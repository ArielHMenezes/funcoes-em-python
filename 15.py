def funcao(numero):
    milhar = numero//1000
    centena = (numero%1000)//100
    dezena = ((numero%1000)%100)//10
    unidade = ((numero%1000)%100)%10
    return milhar, centena, dezena, unidade