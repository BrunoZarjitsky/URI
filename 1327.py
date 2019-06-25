while True:
    qtd = int(input())
    if qtd == 0:
        break
    nomes = input().split(" ")
    nomesSalvos = nomes.copy()
    cartas = []
    for i in range(4):
        cartas.append(input().split(" "))
    cartas = cartas[0]+cartas[1]+cartas[2]+cartas[3]
    cartas = list(map(lambda x: int(x), cartas))
    i = 0
    while len(nomes) != 0:
        amostra = cartas[i:i+len(nomes)]
        i += len(nomes)
        if len(amostra) == 0:
            break
        finais = []
        for j in range(amostra.count(min(amostra))):
            finais.append(nomes[amostra.index(min(amostra))])
            nomes.remove(nomes[amostra.index(min(amostra))])
            amostra.remove(min(amostra))
    finais = finais + nomes
    output = ""
    for i in nomesSalvos:
        if i in finais:
            output += i + " "
    print (output)