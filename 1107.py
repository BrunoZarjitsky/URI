while True:
    qtd = input().split()
    if qtd == ["0", "0"]:
        break
    alt, lar = int(qtd[0]), int(qtd[1])
    seq = input().split()
    seq = list(map(lambda x: int(x), seq))
    total = alt - seq[0]
    continuidade = False
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            total += seq[i-1] - seq[i]
    print (str(total))