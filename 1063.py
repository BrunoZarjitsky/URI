while True:
    qtd = int(input())
    if qtd != 0:
        ladoA = input().split()
        ladoB = input().split()
        saida = ""
        k = 0
        for i in range(len(ladoA)):
            saida += "I"
            if k > len(ladoB)-1:
                break
            if ladoA[i] == ladoB[k]:
                for j in range(i, -1, -1):
                    if k > len(ladoB)-1:
                        break
                    if ladoA[j] == ladoB[k] and ladoA[j] != "1":
                        ladoA[j] = "1"
                        k += 1
                        saida += "R"
                    elif ladoA[j] == "1":
                        continue
                    else:
                        break
        if "".join(ladoA) != "1"*len(ladoA):
            saida += " Impossible"
        print (saida)
    else:
        break