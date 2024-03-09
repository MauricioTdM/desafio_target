DATA_INPUT = 2550

lista = [0, 1]
soma = 0
i = 0
# i = 0
# soma = lista[0 + i] + lista[1 + i]
# lista.append(soma)
# print(lista)
# i = 1
# soma = lista[0 + i] + lista[1 + i]
# lista.append(soma)
# print(lista)
# i = 2
# soma = lista[0 + i] + lista[1 + i]
# lista.append(soma)
# print(lista)

while ENTRADA > soma:
    soma = lista[0 + i] + lista[1 + i]
    lista.append(soma)
    i += 1

print(ENTRADA in lista)