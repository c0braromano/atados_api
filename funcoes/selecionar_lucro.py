def selecionar_lucro(precos):
    maior_lucro = 0
    for posicao in range(len(precos)):
        for preco in precos[posicao:]:
            possivel_lucro = preco - precos[posicao]

            if possivel_lucro > maior_lucro:
                maior_lucro = possivel_lucro

    return maior_lucro