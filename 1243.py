letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "1234567890"
while True:
    try:
        frase = str(input()).split()
        palavras = []
        for i in range(len(frase)):
            palavra = ""
            for j in range(len(frase[i])):
                if frase[i][j] == "." and j+1 != len(frase[i]) or frase[i][j] in numeros:
                    palavra = ""
                    break
                elif frase[i][j] != ".":
                    palavra += frase[i][j]
            if palavra != "":
                palavras.append(palavra)
        soma = 0
        qtd = 0
        for i in palavras:
            soma += len(i)
            qtd += 1
        if len(palavras) == 0:
            print ("250")
            continue
        if soma/qtd < 4:
            print (str(250))
        elif soma/qtd < 6:
            print (str(500))
        else:
            print (str(1000))
    except:
        break
