conversor_texto = ""
quant_de_vog = 0
vogais = "aeiouAEIOU"

texto = input()
sel_char = input()

for char in texto:
    e_vogal = False

    for vog in vogais:
        if vog == char:
            e_vogal = True

    if not e_vogal:
        conversor_texto += char
    else:
        quant_de_vog += 1
        conversor_texto += sel_char


print(quant_de_vog)
print(conversor_texto)