def cj():
    while True:
        try:
            n=input()
            listaD = []
            listaE = []
            for i in range(31):
                listaD.append(0)
                listaE.append(0)
            par=0
            for i in range(n):
                sap=raw_input()
                sap = sap.split(" ")
                pe = sap[1]
                tam = int(sap[0])-31
                if pe == "D":
                    listaD[tam] += 1
                if pe == "E":
                    listaE[tam] += 1
            for i in range(31):
                par += min(listaD[i], listaE[i])
            print par
        except EOFError:
            break

if __name__ == "__main__":
    cj()